# Capteur de Distance Ultrasonique avec ESP32 et Transmission JSON

## Vue d'ensemble du projet
Ce projet utilise un microcontrôleur ESP32 pour mesurer la distance à l'aide d'un capteur ultrasonique et afficher les mesures sur un écran LCD. Les données sont également transmises au format JSON via WiFi.

## Matériel requis
- Microcontrôleur ESP32-WROOM  
- Capteur ultrasonique HC-SR04  
- Écran LCD 16x2 (LM044L)  
- Réseau WiFi  

## Dépendances logicielles
- **ArduinoJson**  
- **WiFi Library**  
- **HTTPClient**  

## Étapes d'installation
1. Installer les bibliothèques nécessaires.  
2. Configurer les identifiants WiFi (SSID et mot de passe).  
3. Définir l'adresse IP du serveur cible.  
4. Téléverser le code dans l'ESP32.  

## Protocole de communication
- Envoie une charge utile JSON toutes les 5 secondes.  
- Structure de la charge utile :  
  ```json
  {
    "distance": 23.45,
    "unit": "cm"
  }
  ```  

## Implémentation du module récepteur
Un module récepteur peut :  
1. Écouter sur un endpoint HTTP spécifié.  
2. Analyser les données JSON reçues.  
3. Traiter les informations sur la distance.  
4. Déclencher des actions en fonction des données de distance.  

## Dépannage
- Vérifiez la connectivité WiFi.  
- Assurez-vous que l'endpoint du serveur est accessible.  
- Surveillez la sortie série pour détecter les erreurs.  