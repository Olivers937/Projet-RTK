# OSM Location Finder

Un module Python pour rechercher et visualiser des emplacements en utilisant OpenStreetMap.
toutes le commandes suivantes devront etre effectuer dans le repertoire geolocalisation ou celui racine mais pour l'installation des dependances bien preciser le chemin vers le requirements.txt de geolocalisation

## Structure du projet
```
project_folder/
│   requirements.txt
│   README.md
│   osm_location_finder.py
│   main.py
|   exec.py 
└───osm_tiles/
        |
        |__data/
        |__maps/
        |__titles/
```

## Configuration de l'environnement

1. Créer un environnement virtuel
```bash
python -m venv venv
```

2. Activer l'environnement virtuel

Sur Windows :
```bash
venv\Scripts\activate
```

Sur Unix/MacOS :
```bash
source venv/bin/activate
```

3. Installer les dépendances
```bash
pip install -r requirements.txt
```

## Utilisation

1. executer le fichier main.py
```bash
python3 main.py

python3 exec.py
```
Les cartes générées (fichiers HTML) s'ouvrent dans votre navigateur web.
