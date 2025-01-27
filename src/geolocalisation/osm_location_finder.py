import os
import json
from typing import Dict, Optional, Tuple, List
import requests
from geopy.geocoders import Nominatim
import folium
from folium import plugins
from pathlib import Path
import time
from datetime import datetime

class OSMLocationFinder:
    def __init__(self, base_path: str = "osm_tiles"):
        """
        Initialise le système de localisation avec un dossier de base pour stocker les données

        Args:
            base_path: Chemin du dossier principal pour stocker les données
        """
        self.geolocator = Nominatim(user_agent="flexible_location_finder")
        self.base_path = Path(base_path)
        self.maps_path = self.base_path / "maps"
        self.data_path = self.base_path / "data"
        self.tiles_path = self.base_path / "tiles"

        # Création des dossiers nécessaires
        for path in [self.base_path, self.maps_path, self.data_path, self.tiles_path]:
            path.mkdir(parents=True, exist_ok=True)

    def _sanitize_filename(self, name: str) -> str:
        """
        Nettoie le nom de fichier pour éviter les caractères spéciaux
        """
        return "".join(c for c in name if c.isalnum() or c in (' ', '-', '_')).strip()

    def _get_location_files(self, query: str) -> Tuple[Path, Path]:
        """
        Génère les chemins de fichiers pour une recherche donnée
        """
        sanitized_name = self._sanitize_filename(query)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        map_file = self.maps_path / f"map_{sanitized_name}_{timestamp}.html"
        data_file = self.data_path / f"data_{sanitized_name}_{timestamp}.json"
        return map_file, data_file

    def download_tiles(self, lat: float, lon: float, zoom: int = 15) -> str:
        """
        Télécharge et met en cache les tuiles OSM pour une zone donnée
        """
        tile_url = f"https://tile.openstreetmap.org/{zoom}/{lat}/{lon}.png"
        tile_name = f"tile_{lat}_{lon}_{zoom}.png"
        tile_path = self.tiles_path / tile_name

        if not tile_path.exists():
            response = requests.get(tile_url)
            if response.status_code == 200:
                with open(tile_path, 'wb') as f:
                    f.write(response.content)
                time.sleep(0.5)  # Respect des limites de l'API OSM

        return str(tile_path)

    def search_location(self, query: str, language: str = "fr") -> Tuple[Optional[Dict], Optional[str]]:
        """
        Recherche une localisation avec une requête flexible

        Args:
            query: Nom du lieu ou adresse à rechercher
            language: Code de langue pour les résultats (ex: 'fr', 'en')

        Returns:
            Tuple contenant les données de localisation et le chemin de la carte
        """
        try:
            # Configuration de la recherche
            location = self.geolocator.geocode(
                query,
                exactly_one=False,
                language=language,
                addressdetails=True,
                namedetails=True
            )

            if not location or len(location) == 0:
                return None, None

            # Prendre le résultat le plus pertinent
            best_location = location[0]

            # Préparation des données enrichies
            location_data = {
                'query': query,
                'timestamp': datetime.now().isoformat(),
                'formatted_address': best_location.address,
                'coordinates': {
                    'latitude': best_location.latitude,
                    'longitude': best_location.longitude
                },
                'place_details': {
                    'name': best_location.raw.get('namedetails', {}).get('name'),
                    'place_id': best_location.raw.get('place_id'),
                    'type': best_location.raw.get('type'),
                    'importance': best_location.raw.get('importance'),
                },
                'address_components': best_location.raw.get('address', {}),
                'alternatives': [
                    {
                        'address': loc.address,
                        'latitude': loc.latitude,
                        'longitude': loc.longitude
                    }
                    for loc in location[1:3]  # Inclure jusqu'à 2 alternatives
                ]
            }

            # Création de la carte interactive
            m = folium.Map(
                location=[best_location.latitude, best_location.longitude],
                zoom_start=15,
                tiles='OpenStreetMap'
            )

            # Ajout des contrôles avancés
            plugins.Fullscreen().add_to(m)
            plugins.LocateControl().add_to(m)
            plugins.MousePosition().add_to(m)
            plugins.MeasureControl().add_to(m)

            # Marqueur principal
            popup_content = f"""
                <div style='font-family: Arial, sans-serif;'>
                    <h4>{query}</h4>
                    <p><b>Adresse:</b> {best_location.address}</p>
                    <p><b>Coordonnées:</b><br>
                    Lat: {best_location.latitude}<br>
                    Lon: {best_location.longitude}</p>
                </div>
            """

            folium.Marker(
                [best_location.latitude, best_location.longitude],
                popup=popup_content,
                icon=folium.Icon(color='red', icon='info-sign')
            ).add_to(m)

            # Ajouter les alternatives sur la carte
            for idx, alt in enumerate(location[1:3]):
                folium.Marker(
                    [alt.latitude, alt.longitude],
                    popup=f"Alternative {idx+1}: {alt.address}",
                    icon=folium.Icon(color='blue', icon='info-sign')
                ).add_to(m)

            # Génération des noms de fichiers
            map_file, data_file = self._get_location_files(query)

            # Sauvegarde de la carte et des données
            m.save(str(map_file))
            with open(data_file, 'w', encoding='utf-8') as f:
                json.dump(location_data, f, ensure_ascii=False, indent=2)

            return location_data, str(map_file)

        except Exception as e:
            print(f"Erreur lors de la recherche: {e}")
            return None, None

    def get_nearby_places(self, lat: float, lon: float, radius: int = 1000) -> List[Dict]:
        """
        Trouve les lieux à proximité des coordonnées données

        Args:
            lat: Latitude
            lon: Longitude
            radius: Rayon de recherche en mètres

        Returns:
            Liste des lieux trouvés
        """
        overpass_url = "http://overpass-api.de/api/interpreter"
        overpass_query = f"""
        [out:json][timeout:25];
        (
          node["amenity"](around:{radius},{lat},{lon});
          way["amenity"](around:{radius},{lat},{lon});
          relation["amenity"](around:{radius},{lat},{lon});
        );
        out body;
        >;
        out skel qt;
        """

        try:
            response = requests.post(overpass_url, data=overpass_query)
            data = response.json()

            places = []
            for element in data.get('elements', []):
                if 'tags' in element:
                    places.append({
                        'type': element.get('type'),
                        'id': element.get('id'),
                        'lat': element.get('lat'),
                        'lon': element.get('lon'),
                        'tags': element.get('tags')
                    })

            return places

        except Exception as e:
            print(f"Erreur lors de la recherche des lieux proches: {e}")
            return []

    def visualize_coordinates(self, lat: float, lon: float, title: str = "Location") -> str:
        """
        Crée une carte interactive pour des coordonnées données

        Args:
            lat: Latitude
            lon: Longitude
            title: Titre à afficher sur le marqueur

        Returns:
            Chemin du fichier de la carte générée
        """
        # Création de la carte
        m = folium.Map(
            location=[lat, lon],
            zoom_start=15,
            tiles='OpenStreetMap'
        )

        # Ajout des contrôles
        plugins.Fullscreen().add_to(m)
        plugins.LocateControl().add_to(m)
        plugins.MousePosition().add_to(m)
        plugins.MeasureControl().add_to(m)

        # Création du popup
        popup_content = f"""
            <div style='font-family: Arial, sans-serif;'>
                <h4>{title}</h4>
                <p><b>Coordonnées:</b><br>
                Lat: {lat}<br>
                Lon: {lon}</p>
            </div>
        """

        # Ajout du marqueur
        folium.Marker(
            [lat, lon],
            popup=popup_content,
            icon=folium.Icon(color='red', icon='info-sign')
        ).add_to(m)

        # Ajout d'un cercle
        folium.Circle(
            [lat, lon],
            radius=100,  # rayon en mètres
            color='blue',
            fill=True,
            popup='Rayon de 100m'
        ).add_to(m)

        # Génération du nom de fichier avec timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        sanitized_title = self._sanitize_filename(title)
        map_file = self.maps_path / f"coordinates_{sanitized_title}_{timestamp}.html"

        # Sauvegarde de la carte
        m.save(str(map_file))

        return str(map_file)

if __name__ == "__main__":
    finder = OSMLocationFinder()

    # Exemple de recherche flexible
    location_data, map_path = finder.search_location("Tour Eiffel")
    if location_data:
        print(f"Données sauvegardées dans: {map_path}")

        # Recherche des lieux à proximité
        if location_data['coordinates']:
            nearby = finder.get_nearby_places(
                location_data['coordinates']['latitude'],
                location_data['coordinates']['longitude']
            )
            print(f"Nombre de lieux trouvés à proximité: {len(nearby)}")

