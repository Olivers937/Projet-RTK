# 🛰️ Projet RTK 
## Système de Géolocalisation de Précision
*Polytechnique Yaoundé - 4ème année Génie Informatique*

*Unité d'enseignement : Électronique et Interfaçage*  
*Superviseur : Dr. CHANA Anne Marie*

## Table des matières
1. [À propos du projet](#à-propos-du-projet)
2. [Objectifs du projet](#objectifs-du-projet)
3. [Contexte technologique](#contexte-technologique)
4. [Applications visées](#applications-visées)
5. [Spécifications techniques](#spécifications-techniques)
6. [Architecture du système](#architecture-du-système)
7. [État d'avancement](#état-davancement)
8. [Structure du Repository](#structure-du-repository)
9. [Équipe du projet](#équipe-du-projet)
10. [Contribution](#contribution)
11. [Contact](#contact)
12. [Licence](#licence)

## À propos du projet
Le RTK (Real Time Kinematic) est une technologie de pointe qui révolutionne la géolocalisation de précision à travers le monde. Déjà largement utilisée dans l'agriculture de précision en Europe et en Amérique du Nord, cette technologie permet notamment aux agriculteurs d'optimiser leurs opérations avec une précision centimétrique. Elle est également déployée dans des domaines aussi variés que la construction intelligente, la cartographie haute précision et même la conduite autonome.

Dans le cadre de notre formation à Polytechnique Yaoundé, notre groupe d'étudiants en 4ème année de Génie Informatique entreprend d'adapter cette technologie pour répondre aux besoins spécifiques de notre communauté camerounaise. Notre projet vise à implémenter un système RTK accessible et adapté au contexte local, permettant d'explorer les possibilités d'applications dans l'agriculture, la topographie et l'urbanisme en Afrique.

## Objectifs du projet
* Développer un réseau de bases GNSS accessible et abordable
* Fournir une solution de géolocalisation précise pour les applications locales
* Contribuer à l'innovation technologique dans notre région
* Créer une base de connaissances pour les futures générations d'étudiants

## Contexte technologique
Le RTK (Real Time Kinematic) est une technologie de positionnement par satellite qui permet d'obtenir une précision centimétrique en temps réel. Notre système utilise :

* Des signaux GPS, GLONASS et Galileo
* Une station de base fixe
* Des récepteurs mobiles
* Un système de correction en temps réel

## Applications visées
Notre solution pourra servir dans plusieurs domaines critiques pour le développement local :

1. Agriculture de précision
2. Cartographie urbaine
3. Travaux publics
4. Surveillance environnementale
5. Études topographiques

## Spécifications techniques
```
Précision horizontale : ~1 cm
Précision verticale : ~2 cm
Couverture : Zone métropolitaine de Yaoundé (extensible)
Temps de réponse : Temps réel
```

## Architecture du système

### 1. Station de base
* Position fixe et connue
* Calcul des corrections
* Transmission des données

### 2. Unités mobiles
* Réception des signaux GNSS
* Application des corrections
* Calcul de position précise

### 3. Système de communication
* Transmission en temps réel
* Protocoles sécurisés
* Gestion de la bande passante

## État d'avancement
- [x] Étude de faisabilité
- [x] Conception du système
- [ ] Développement du prototype
- [ ] Tests sur le terrain
- [ ] Déploiement pilote

## Équipe du projet
Notre équipe est composée d'étudiants passionnés par l'innovation technologique et déterminés à apporter des solutions concrètes aux défis de notre société.
| NOM | Matricule |
|-----------|-----------|
| MEKIAGE Olivier (Chef de groupe) | 21p** |
| KUATE KAMGA Brayan | 21p130 |
| NGUEPSSI Brayanne | 23P780 |
| NTYE EBO’O Nina |  21P223 |
| VUIDE OUENDEU Jordan | 21P018 |
| KOUASSI DE YOBO G. Bryan | 21P082 |
| LEMOBENG NGOUANE Belviane | 21P187 | 
| FEZEU YOUNDJE Fredy Clinton | 23P751 |
| BADA RODOLPHE Andre | 21P233 |
| DANGA PATCHOUM Blonde | 21P169 |

## Structure du Repository

Notre repository est organisé de manière à faciliter l'accès aux différentes ressources du projet. Voici la structure détaillée :

```
📁 Projet-RTK/
├── 📁 Documentation/
│   ├── 📄 document_de_conception.pdf
│   ├── 📄 guide_installation.pdf
│   └── 📄 guide_de_deploiement.pdf
│
├── 📁 Rapports_Hebdomadaires/
│   ├── 📁 Semaine_1/
│   │   ├── 📄 rapport_s1.docx
│   │   ├── 📁 images/
│   │   └── 📁 videos/
│   ├── 📁 Semaine_2/
│   └── ...
│
├── 📁 Source/
│   ├── 📁 station_base/
│   ├── 📁 unite_mobile/
│   └── 📁 interface_utilisateur/
│
├── 📁 Tests/
│   ├── 📁 tests_unitaires/
│   └── 📁 tests_integration/
│
├── 📄 README.md
└── 📄 LICENSE.md
```

### Guide de Navigation

1. **Documentation/**
   * Contient toute la documentation technique du projet
   * Les guides d'installation et d'utilisation
   * Les spécifications détaillées

2. **Rapports_Hebdomadaires/**
   * Organisé par semaine
   * Chaque dossier hebdomadaire contient :
     * Un rapport détaillé au format Markdown
     * Un sous-dossier `images/` pour les captures d'écran et photos
     * Un sous-dossier `videos/` pour les démonstrations
   * Permet de suivre la progression chronologique du projet

3. **Source/**
   * Contient tout le code source du projet
   * Organisé par composants majeurs du système

4. **Tests/**
   * Contient les tests unitaires et d'intégration
   * Documentation des procédures de test

## Contribution
Nous encourageons les contributions de la communauté universitaire et des professionnels du secteur. Pour contribuer :

1. Fork le projet
2. Créez votre branche (`git checkout -b feature/AmazingFeature`)
3. Committez vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrez une Pull Request

## Contact
Pour plus d'informations sur le projet, contactez l'équipe de développement à Polytechnique Yaoundé.

## Licence
Ce projet est sous licence MIT - voir le fichier [LICENSE.md](LICENSE.md) pour plus de détails.

---
*Projet développé dans le cadre de l'UE Électronique et Interfaçage*  
*Département de Génie Informatique*  
*Polytechnique Yaoundé, 2024*
