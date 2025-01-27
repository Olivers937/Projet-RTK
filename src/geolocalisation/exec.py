from osm_location_finder import OSMLocationFinder
import sys
from pathlib import Path

def print_separator():
    """Affiche une ligne de séparation"""
    print("\n" + "="*50 + "\n")

def print_location_details(location_data):
    """Affiche les détails de la localisation de manière formatée"""
    if not location_data:
        print("❌ Aucune information trouvée pour ce lieu.")
        return

    print("\n📍 DÉTAILS DE LA LOCALISATION")
    print_separator()

    print(f"📌 Adresse complète: {location_data['formatted_address']}")
    print(f"🌍 Coordonnées: {location_data['coordinates']['latitude']}, {location_data['coordinates']['longitude']}")

    if location_data['address_components']:
        print("\n📑 COMPOSANTS DE L'ADRESSE:")
        for key, value in location_data['address_components'].items():
            print(f"  • {key}: {value}")

    if location_data['alternatives']:
        print("\n🔄 AUTRES RÉSULTATS POSSIBLES:")
        for i, alt in enumerate(location_data['alternatives'], 1):
            print(f"  {i}. {alt['address']}")

def print_nearby_places(places):
    """Affiche les lieux à proximité de manière formatée"""
    if not places:
        print("\n❌ Aucun lieu trouvé à proximité.")
        return

    print("\n🏢 LIEUX À PROXIMITÉ")
    print_separator()

    for i, place in enumerate(places[:10], 1):  # Limite aux 10 premiers résultats
        if 'tags' in place and 'name' in place['tags']:
            name = place['tags'].get('name', 'Sans nom')
            type_lieu = place['tags'].get('amenity', 'Non catégorisé')
            print(f"{i}. {name} ({type_lieu})")

def main():
    try:
        finder = OSMLocationFinder()

        print("\n🔍 RECHERCHE DE LOCALISATION")
        print_separator()
        print("Entrez le nom du lieu à rechercher (ou 'q' pour quitter):")

        while True:
            query = input("\n➤ ").strip()

            if query.lower() in ['q', 'quit', 'exit']:
                print("\n👋 Au revoir!")
                break

            if not query:
                print("⚠️  Veuillez entrer un lieu à rechercher.")
                continue

            print("\n🔄 Recherche en cours...")

            # Recherche du lieu
            location_data, map_path = finder.search_location(query)

            if location_data and map_path:
                print(f"\n✅ Recherche terminée!")
                print(f"📂 Carte générée: {map_path}")
                data_path = Path(map_path).parent.parent / "data"
                data_files = list(data_path.glob(f"data_{Path(map_path).stem}*.json"))
                if data_files:
                    print(f"📄 Données JSON: {data_files[0]}")

                # Affichage des détails
                print_location_details(location_data)

                # Recherche des lieux à proximité
                print("\n🔄 Recherche des lieux à proximité...")
                nearby_places = finder.get_nearby_places(
                    location_data['coordinates']['latitude'],
                    location_data['coordinates']['longitude'],
                    radius=500
                )
                print_nearby_places(nearby_places)

            else:
                print("\n❌ Désolé, aucun résultat trouvé pour cette recherche.")

            print_separator()
            print("Entrez un autre lieu à rechercher (ou 'q' pour quitter):")

    except KeyboardInterrupt:
        print("\n\n👋 Programme interrompu par l'utilisateur.")
    except Exception as e:
        print(f"\n❌ Une erreur est survenue: {e}")
    finally:
        sys.exit(0)

if __name__ == "__main__":
    main()
