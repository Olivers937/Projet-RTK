from osm_location_finder import OSMLocationFinder
import json
from pathlib import Path

def print_location_info(location_data):
    """Affiche les informations de localisation de manière formatée"""
    if location_data:
        print("\nInformations de localisation:")
        print(f"Adresse: {location_data['formatted_address']}")
        print(f"Coordonnées: {location_data['coordinates']['latitude']}, {location_data['coordinates']['longitude']}")
        if location_data['address_components']:
            print("\nDétails de l'adresse:")
            for key, value in location_data['address_components'].items():
                print(f"  {key}: {value}")

        if location_data['alternatives']:
            print("\nLocalisations alternatives trouvées:")
            for i, alt in enumerate(location_data['alternatives'], 1):
                print(f"  {i}. {alt['address']}")

def main():
    # Initialisation du finder avec un dossier spécifique
    finder = OSMLocationFinder(base_path="osm_tiles")

    # Recherche de l'ENSPY
    print("\nRecherche du lieu...")
    location_data, map_path = finder.search_location("université de yaounde 1", language="fr")

    if location_data and map_path:
        print(f"\nCarte générée: {map_path}")
        print_location_info(location_data)

        # Recherche des lieux à proximité
        print("\nRecherche des lieux à proximité...")
        nearby_places = finder.get_nearby_places(
            location_data['coordinates']['latitude'],
            location_data['coordinates']['longitude'],
            radius=500  # Rayon de 500 mètres
        )

        if nearby_places:
            print(f"\nLieux trouvés à proximité ({len(nearby_places)}):")
            for place in nearby_places[:5]:  # Afficher les 5 premiers lieux
                if 'tags' in place and 'name' in place['tags']:
                    print(f"  - {place['tags'].get('name', 'Sans nom')} "
                          f"({place['tags'].get('amenity', 'Non catégorisé')})")
    else:
        print("Aucune donnée trouvée pour l'ENSPY")

    # Exemple avec des coordonnées spécifiques
    print("\nCréation d'une carte pour des coordonnées spécifiques...")
    custom_location = {
        'name': "Localisation personnalisée",
        'latitude': 3.8667,  # Coordonnées de Yaoundé
        'longitude': 11.5167
    }

    map_path = finder.visualize_coordinates(
        custom_location['latitude'],
        custom_location['longitude'],
        custom_location['name']
    )
    print(f"Carte des coordonnées générée: {map_path}")

    # Recherche des lieux à proximité des coordonnées spécifiques
    print("\nRecherche des lieux à proximité des coordonnées spécifiques...")
    nearby_places = finder.get_nearby_places(
        custom_location['latitude'],
        custom_location['longitude'],
        radius=1000  # Rayon de 1 km
    )

    if nearby_places:
        print(f"\nLieux trouvés à proximité ({len(nearby_places)}):")
        for place in nearby_places[:5]:  # Afficher les 5 premiers lieux
            if 'tags' in place and 'name' in place['tags']:
                print(f"  - {place['tags'].get('name', 'Sans nom')} "
                      f"({place['tags'].get('amenity', 'Non catégorisé')})")

if __name__ == "__main__":
    main()
