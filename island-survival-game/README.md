# Lonely Island 🏝️

Un jeu de survie en mode texte où vous devez survivre le plus longtemps possible sur une île déserte en gérant votre *faim*, votre *soif* et votre *énergie*.

## 📋 Table des matières

- [Fonctionnalités](#fonctionnalités)
- [Prérequis](#prérequis)
- [Installation](#installation)
- [Comment jouer](#comment-jouer)
- [Structure du projet](#structure-du-projet)
- [Système de difficulté](#système-de-difficulté)
- [Actions disponibles](#actions-disponibles)
- [Événements aléatoires](#événements-aléatoires)
- [Sauvegarde et chargement](#sauvegarde-et-chargement)
- [Contribuer](#contribuer)
- [Licence](#licence)

## ✨ Fonctionnalités

- **6 niveaux de difficulté** : Baby, Easy, Medium, Hard, Hardcore, Nightmare
- **Système de jauges** : Gérez votre faim, soif et énergie
- **Actions variées** : Chasser, pêcher, chercher de l'eau, dormir, explorer
- **Événements aléatoires** : Tempêtes, découvertes, blessures...
- **Système de sauvegarde** : Sauvegardez et chargez vos parties à tout moment
- **Progression dynamique** : La difficulté augmente avec les jours
- **Interface textuelle claire** : Barres de progression visuelles

## 🔧 Prérequis

- Python 3.8 ou supérieur
- Système d'exploitation : Windows, macOS ou Linux

## 📦 Installation

1. Clonez le dépôt :
```bash
git clone https://github.com/votre-username/island-survival-game.git
cd island-survival-game
```

2. Aucune dépendance externe n'est requise (utilise uniquement la bibliothèque standard Python)

## 🎮 Comment jouer

### Lancer le jeu

**Windows :**
```bash
cd src
python __main__.py
```

**macOS/Linux :**
```bash
cd src
python3 __main__.py
```

### Démarrer une partie

1. Entrez le nom de votre personnage
2. Sélectionnez un niveau de difficulté (1-6)
3. Survivez le plus longtemps possible !

### Objectif

Survivez le plus de jours possible en maintenant vos jauges dans des limites acceptables :
- **Faim** : Ne doit pas atteindre 100
- **Soif** : Ne doit pas atteindre 100
- **Énergie** : Ne doit pas descendre à 0

## 📁 Structure du projet

```
island-survival-game/
├── src/
│   ├── __main__.py           # Point d'entrée du jeu
│   ├── game.py               # Logique principale du jeu
│   ├── player.py             # Classe Player et actions
│   ├── gauges.py             # Système de jauges
│   ├── player_actions.py     # Gestion des actions du joueur
│   ├── main_menu.py          # Menu principal
│   ├── difficulty_manager.py # Gestion de la difficulté
│   ├── random_events.py      # Événements aléatoires
│   ├── save_manager.py       # Sauvegarde/chargement
│   └── utils.py              # Fonctions utilitaires
├── res/
│   ├── difficulty_player.json # Configuration difficulté joueur
│   ├── difficulty_world.json  # Configuration difficulté monde
│   └── random_events.json     # Définition des événements
├── saves/                     # Dossier des sauvegardes (généré)
├── logs/                      # Logs d'erreurs (généré)
└── README.md
```

## 🎯 Système de difficulté

### Niveaux disponibles

| Niveau | Détérioration | Coût énergie | Jours limite | Croissance |
|--------|--------------|--------------|--------------|------------|
| Baby | 0.5 | 5 | 100 | 0.01 |
| Easy | 1.0 | 7 | 75 | 0.02 |
| Medium | 1.5 | 10 | 50 | 0.03 |
| Hard | 2.0 | 15 | 40 | 0.04 |
| Hardcore | 2.5 | 20 | 30 | 0.05 |
| Nightmare | 3.0 | 25 | 20 | 0.06 |

### Progression

La difficulté augmente automatiquement chaque jour selon la formule :
```
détérioration_jour = détérioration_base × (1 + taux_croissance)^jours
```

## 🎲 Actions disponibles

### 1. Chasser 🏹
- **Effet** : Réduit la faim
- **Coût** : Consomme de l'énergie

### 2. Pêcher 🎣
- **Effet** : Réduit la faim
- **Coût** : Consomme de l'énergie

### 3. Chercher de l'eau 💧
- **Effet** : Réduit la soif
- **Coût** : Consomme de l'énergie

### 4. Dormir 😴
- **Effet** : Restaure l'énergie, augmente légèrement faim et soif
- **Coût** : Aucun

### 5. Explorer 🔍
- **Effet** : Événement aléatoire (nourriture, eau, danger ou rien)
- **Coût** : Consomme de l'énergie
- **Chances** :
  - 10% : Trouver de la nourriture
  - 10% : Trouver de l'eau
  - 20% : Rencontre dangereuse (blessure)
  - 60% : Rien ne se passe

### 6. Menu Principal 📋
- Accès aux options de sauvegarde/chargement
- Quitter le jeu

## 🌪️ Événements aléatoires

Chaque jour, un événement peut se produire :

| Événement | Chance | Effet |
|-----------|--------|-------|
| Rien | 50% | Légère perte d'énergie |
| Tempête soudaine | 10% | Perte d'énergie (15) |
| Source d'eau fraîche | 10% | Soif -20 |
| Baies comestibles | 10% | Faim -25 |
| Blessure légère | 10% | Énergie -10 |
| Repos paisible | 10% | Énergie +20 |

## 💾 Sauvegarde et chargement

### Sauvegarder une partie

1. Accédez au menu principal (touche M)
2. Sélectionnez "Sauvegarder la Partie" (option 3)
3. La sauvegarde est horodatée automatiquement

### Charger une partie

1. Au menu principal, sélectionnez "Charger une Partie" (option 4)
2. Choisissez la sauvegarde dans la liste
3. La partie reprend exactement où vous l'avez laissée

### Format de sauvegarde

Les sauvegardes sont stockées au format JSON dans `saves/` :
```json
{
  "save_name": "20251026_143022",
  "player": {
    "name": "Survivant",
    "hunger": 45,
    "thirst": 30,
    "energy": 65,
    "days_survived": 12
  },
  "game": {
    "difficulty": "Medium"
  }
}
```

## 🛠️ Développement

### Ajouter un nouvel événement

Modifiez `res/random_events.json` :
```json
{
  "id": 6,
  "name": "Votre événement",
  "description": "Description de l'événement",
  "effect": {
    "type": "hunger_decrease",
    "cost": 15
  },
  "chance": 85
}
```

### Types d'effets disponibles

- `hunger_increase` / `hunger_decrease`
- `thirst_increase` / `thirst_decrease`
- `energy_increase` / `energy_decrease`

### Logs d'erreurs

Les erreurs sont automatiquement enregistrées dans `logs/error_log.txt` avec horodatage.

## 🤝 Contribuer

Les contributions sont les bienvenues ! Pour contribuer :

1. Forkez le projet
2. Créez une branche pour votre fonctionnalité (`git checkout -b feature/AmazingFeature`)
3. Committez vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Poussez vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrez une Pull Request

### Guidelines

- Respectez la structure du code existant
- Commentez les fonctions complexes
- Testez vos modifications sur tous les niveaux de difficulté
- Mettez à jour la documentation si nécessaire

## 📝 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## 👥 Auteurs

- **DantesDels** - *Développeur principal* - [Lien Github](https://github.com/DantesDels)

## 🙏 Remerciements

- Inspiré par les jeux de survie classiques
- Merci à tous les contributeurs

## 📞 Support

Pour toute question ou problème :
- Ouvrez une [issue](https://github.com/votre-username/island-survival-game/issues)
- Contactez-nous par email : votre-email@example.com

---

**Bon jeu et bonne survie ! 🏝️**