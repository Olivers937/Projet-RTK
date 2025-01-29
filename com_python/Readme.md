# Documentation de l'API de Synthèse et Reconnaissance Vocale

## Introduction

Cette API Flask permet de :

- Lire un texte à voix haute
- Lire le contenu d'un fichier
- Enregistrer un audio
- Reconnaître la parole à partir d'un fichier audio

## Base URL

L'API est accessible localement via :

```
http://127.0.0.1:5000
```

## Routes de l'API

| **Méthode** | **Endpoint**        | **Description**                                 | **Paramètres JSON**                          |
| ----------- | ------------------- | ----------------------------------------------- | -------------------------------------------- |
| POST        | `/read-text`        | Lit un texte fourni                             | `{ "text": "Bonjour" }`                      |
| POST        | `/read-file`        | Lit le contenu d'un fichier                     | `{ "filename": "mon_fichier.txt" }`          |
| POST        | `/record-audio`     | Enregistre un audio pendant une durée spécifiée | `{ "filename": "audio.wav", "duration": 5 }` |
| POST        | `/recognize-speech` | Convertit un fichier audio en texte             | `{ "filename": "audio.wav" }`                |

## Détails des Endpoints

### 1. Lire un Texte à Voix Haute

**URL:** `/read-text`

**Méthode:** `POST`

**Exemple de requête :**

```json
{
  "text": "Bonjour, comment allez-vous ?"
}
```

**Réponse :**

```json
{
  "message": "Texte lu avec succès"
}
```

---

### 2. Lire un Fichier

**URL:** `/read-file`

**Méthode:** `POST`

**Exemple de requête :**

```json
{
  "filename": "text.txt"
}
```

**Réponse :**

```json
{
  "message": "Fichier lu avec succès"
}
```

**Erreurs possibles:**

- `404` : Fichier introuvable

---

### 3. Enregistrer un Audio

**URL:** `/record-audio`

**Méthode:** `POST`

**Exemple de requête :**

```json
{
  "filename": "audio.wav",
  "duration": 5
}
```

**Réponse :**

```json
{
  "message": "Enregistrement terminé"
}
```

**Erreurs possibles:**

- `400` : Paramètres manquants

---

### 4. Reconnaissance Vocale

**URL:** `/recognize-speech`

**Méthode:** `POST`

**Exemple de requête :**

```json
{
  "filename": "audio.wav"
}
```

**Réponse :**

```json
{
  "message": "Texte reconnu",
  "text": "Bonjour tout le monde"
}
```

**Erreurs possibles:**

- `404` : Fichier introuvable
- `400` : Impossible de reconnaître l'audio
- `500` : Erreur du service de reconnaissance

## Lancement de l'API

Pour exécuter l'API, utilisez la commande suivante :

```bash
python app.py
```

L'API démarrera en mode debug sur `http://127.0.0.1:5000`.
