# Island Survival Game 🏝️
*Dernière mise à jour : Octobre 2025*
Un jeu de survie en mode texte où vous devez survivre le plus longtemps possible sur une île déserte en gérant votre faim, votre soif et votre énergie.

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
- [Roadmap](#roadmap)
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
│   ├── random_events.json     # Définition des événements
│   └── ascii_art/            # Art ASCII (à venir)
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

## 🗺️ Roadmap

### Version 1.1 - ASCII Art 🎨
**Statut** : 📋 Planifié | **Date estimée** : Q1 2026

#### Objectifs
- [ ] Intégration d'ASCII art pour tous les événements aléatoires
- [ ] ASCII art pour chaque action du joueur (chasse, pêche, etc.)
- [ ] Écran de titre avec logo du jeu
- [ ] Illustrations pour les niveaux de difficulté
- [ ] ASCII art pour les états critiques (faim/soif/énergie)
- [ ] Animations de transition entre les jours

#### Implémentation technique
```
res/
└── ascii_art/
    ├── events/
    │   ├── storm.txt
    │   ├── water_source.txt
    │   └── berries.txt
    ├── actions/
    │   ├── hunting.txt
    │   ├── fishing.txt
    │   ├── water_search.txt
    │   ├── sleeping.txt
    │   └── exploring.txt
    ├── ui/
    │   ├── title.txt
    │   └── game_over.txt
    └── difficulty/
        ├── baby.txt
        └── nightmare.txt
```

#### Exemple d'intégration
```python
def display_ascii_art(art_name):
    """Affiche l'art ASCII depuis le fichier correspondant"""
    filepath = f'../res/ascii_art/{art_name}.txt'
    with open(filepath, 'r', encoding='utf-8') as file:
        print(file.read())
```

---

### Version 1.2 - Mini-jeux 🎮
**Statut** : 📋 Planifié | **Date estimée** : Q2 2026

#### Objectifs
Transformer chaque action en mini-jeu interactif pour une expérience plus immersive.

#### 1. Chasse 🏹
**Type** : Jeu de timing et de précision
- [ ] Affichage d'une cible en mouvement (ASCII)
- [ ] Le joueur doit appuyer sur une touche au bon moment
- [ ] 3 niveaux de difficulté basés sur la vitesse
- [ ] Récompenses variables selon la performance :
  - Excellent : Faim -30, énergie -5
  - Bon : Faim -20, énergie -10
  - Raté : Faim +5, énergie -15

```
    🦌 ← Appuyez sur ESPACE maintenant !
    [====|====] (zone de réussite)
```

#### 2. Pêche 🎣
**Type** : Jeu de réflexes
- [ ] Séquence de touches aléatoires à reproduire
- [ ] Temps limité pour chaque touche
- [ ] Longueur de séquence selon difficulté
- [ ] Poissons de différentes tailles selon performance :
  - Gros poisson : Faim -25, énergie -8
  - Poisson moyen : Faim -15, énergie -10
  - Petit poisson : Faim -10, énergie -12
  - Rien : Énergie -15

```
    🎣 Reproduisez : W → A → S → D
    Votre saisie : W → A → _
    Temps restant : ▓▓▓▓▓░░░ (5s)
```

#### 3. Chercher de l'eau 💧
**Type** : Jeu d'exploration
- [ ] Grille 5x5 à explorer
- [ ] Sources d'eau cachées (3-5 cases)
- [ ] Nombre de coups limité
- [ ] Indices de proximité (chaud/froid)
- [ ] Récompenses :
  - Source pure : Soif -30, énergie -5
  - Source trouble : Soif -15, énergie -10
  - Aucune source : Soif +5, énergie -15

```
    [?][?][?][?][?]
    [?][X][?][?][?]  X = déjà exploré
    [?][?][💧][?][?]  💧 = eau trouvée
    [?][?][?][?][?]
    [?][?][?][?][?]
    
    Indice : L'eau est proche ! (2 cases)
```

#### 4. Dormir 😴
**Type** : Jeu de rythme
- [ ] Séquence de respiration à suivre
- [ ] Appuyez/relâchez ESPACE selon le rythme
- [ ] 5-8 cycles de respiration
- [ ] Qualité du sommeil selon performance :
  - Excellent : Énergie +30, faim -5, soif -5
  - Bon : Énergie +20, faim -8, soif -8
  - Mauvais : Énergie +10, faim -12, soif -12

```
    ~~~~ Inspirez ~~~~
    [▓▓▓▓▓▓▓▓░░░░]
    
    Maintenez ESPACE...
    
    ~~~~ Expirez ~~~~
    [▓▓▓▓░░░░░░░░]
```

#### 5. Explorer 🔍
**Type** : Jeu de choix multiples
- [ ] 3 chemins possibles à chaque étape
- [ ] Série de 3-5 décisions
- [ ] Conséquences cumulatives
- [ ] Résultat final selon le parcours
- [ ] Événements spéciaux débloquables

```
    Vous arrivez à une bifurcation...
    
    A) Suivre la côte (sûr mais long)
    B) Traverser la jungle (risqué mais rapide)
    C) Grimper la colline (vue d'ensemble)
    
    Votre choix : _
```

#### Implémentation technique
```
src/
└── minigames/
    ├── __init__.py
    ├── hunting_game.py
    ├── fishing_game.py
    ├── water_search_game.py
    ├── sleeping_game.py
    ├── exploring_game.py
    └── minigame_base.py  # Classe abstraite
```

#### Système de score
- [ ] Statistiques globales sauvegardées
- [ ] Classement des meilleures performances
- [ ] Déblocage de bonus selon niveau de maîtrise

---

### Version 1.3 - Amélioration de l'UI 🎨
**Statut** : 📋 Planifié | **Date estimée** : Q3 2026

#### Objectifs généraux
- [ ] Interface plus intuitive et visuellement attrayante
- [ ] Animations et transitions fluides
- [ ] Meilleure lisibilité des informations
- [ ] Feedback visuel renforcé
- [ ] Thèmes de couleurs personnalisables

#### 1. Dashboard amélioré

**Avant :**
```
Survivant — Hunger: 45, Thirst: 30, Energy: 65, Days: 12
```

**Après :**
```
╔════════════════════════════════════════════════════════════╗
║               🏝️    LONELY ISLAND     🏝️                  ║
║                    Jour 12 - Medium                        ║
╠════════════════════════════════════════════════════════════╣
║  👤 Survivant                      🌡️ Température: 28°C   ║
║                                                            ║
║  🍖 Faim    [████████████░░░░░░░░] 45/100  ⚠️             ║
║  💧 Soif    [████████░░░░░░░░░░░░] 30/100  ✓              ║
║  ⚡ Énergie [█████████████░░░░░░░] 65/100  ✓              ║
║                                                            ║
║  📊 Statut: En forme      🎯 Record: 25 jours             ║
╚════════════════════════════════════════════════════════════╝
```

#### 2. Menu contextuel interactif

**Fonctionnalités :**
- [ ] Raccourcis clavier visuels
- [ ] Prévisualisation des effets d'action
- [ ] Indicateurs de coût/bénéfice
- [ ] Conseils basés sur l'état actuel

```
╔════════════════════ ACTIONS ════════════════════╗
║                                                  ║
║  [1] 🏹 Chasser          Énergie: -10  Faim: ↓  ║
║      └─ Recommandé : Faim élevée                ║
║                                                  ║
║  [2] 🎣 Pêcher           Énergie: -10  Faim: ↓  ║
║      └─ Alternative à la chasse                 ║
║                                                  ║
║  [3] 💧 Eau             Énergie: -10  Soif: ↓   ║
║      └─ ⚠️ PRIORITAIRE : Soif critique !        ║
║                                                  ║
║  [4] 😴 Dormir          Énergie: ↑   Faim/Soif:↑║
║      └─ Repos nécessaire                        ║
║                                                  ║
║  [5] 🔍 Explorer        Énergie: -15  ???       ║
║      └─ Risqué mais potentiellement rentable    ║
║                                                  ║
║  [M] 📋 Menu            [Q] Quitter              ║
╚══════════════════════════════════════════════════╝
```

#### 3. Système de notifications

**Types de notifications :**
- [ ] Alertes critiques (jauges dangereuses)
- [ ] Accomplissements (nouveaux records)
- [ ] Événements spéciaux
- [ ] Conseils contextuels

```
┌─────────────────────────────────────┐
│ ⚠️  ALERTE CRITIQUE                │
│                                     │
│ Votre soif atteint un niveau        │
│ dangereux (85/100) !                │
│                                     │
│ 💡 Conseil : Cherchez de l'eau     │
│    avant la fin du jour.            │
└─────────────────────────────────────┘
```

#### 4. Écran de fin de partie amélioré

```
╔════════════════════════════════════════════════════════════╗
║                                                            ║
║                    ☠️  GAME OVER  ☠️                      ║
║                                                            ║
║              Vous avez survécu 18 jours                    ║
║                                                            ║
╠════════════════════════════════════════════════════════════╣
║                                                            ║
║  📊 STATISTIQUES DE LA PARTIE                              ║
║                                                            ║
║  🏆 Meilleur jour :           Jour 15                     ║
║  🎯 Actions réussies :        42 / 54  (77%)              ║
║  🌟 Événements positifs :     8                           ║
║  ⚠️  Événements négatifs :    6                           ║
║  🏹 Chasses réussies :        12                          ║
║  🎣 Pêches réussies :         8                           ║
║  💧 Eau trouvée :             15 fois                     ║
║  😴 Nuits de sommeil :        18                          ║
║  🔍 Explorations :            7                           ║
║                                                            ║
║  Cause du décès : Déshydratation                           ║
║                                                            ║
╠════════════════════════════════════════════════════════════╣
║                                                            ║
║  🏅 CLASSEMENT                                            ║
║                                                           ║
║  1. Record personnel :     25 jours  (Medium)             ║
║  2. Cette partie :         18 jours  (Medium)             ║
║  3. Moyenne :              14 jours                       ║
║                                                            ║
╠════════════════════════════════════════════════════════════╣
║                                                            ║
║  [R] Rejouer    [M] Menu    [Q] Quitter                    ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝
```

#### 5. Thèmes de couleurs (avec `colorama`)

**Thèmes disponibles :**
- [ ] Classique (noir/blanc)
- [ ] Tropical (vert/bleu)
- [ ] Crépuscule (orange/violet)
- [ ] Nuit (bleu foncé)
- [ ] Désert (jaune/brun)

**Dépendance optionnelle :**
```bash
pip install colorama
```

#### 6. Animations et transitions

**Éléments animés :**
- [ ] Chargement avec barre de progression
- [ ] Transition jour/nuit
- [ ] Effet de "typing" pour les messages importants
- [ ] Clignotement pour les alertes critiques
- [ ] Animation des jauges lors des changements

```python
# Exemple d'animation de jauge
def animate_gauge_change(gauge, old_value, new_value):
    steps = 10
    for i in range(steps + 1):
        current = old_value + (new_value - old_value) * (i / steps)
        display_gauge(gauge, current)
        time.sleep(0.05)
```

#### 7. Aide contextuelle intégrée

**Fonctionnalités :**
- [ ] Touche [?] pour aide contextuelle
- [ ] Tutoriel interactif pour nouveaux joueurs
- [ ] Glossaire des termes
- [ ] FAQ intégrée

```
╔════════════════ AIDE [1/5] ════════════════╗
║                                            ║
║  🎯 OBJECTIF DU JEU                       ║
║                                            ║
║  Survivez le plus longtemps possible      ║
║  sur une île déserte en gérant :          ║
║                                            ║
║  • 🍖 Votre faim                          ║
║  • 💧 Votre soif                          ║
║  • ⚡ Votre énergie                        ║
║                                            ║
║  [←] Précédent  [→] Suivant  [ESC] Fermer║
╚════════════════════════════════════════════╝
```

#### Implémentation technique

```
src/
└── ui/
    ├── __init__.py
    ├── theme_manager.py      # Gestion des thèmes
    ├── animations.py          # Animations et transitions
    ├── dashboard.py           # Dashboard principal
    ├── notifications.py       # Système de notifications
    ├── game_over_screen.py    # Écran de fin
    └── help_system.py         # Système d'aide
```

#### Performance et accessibilité
- [ ] Mode performance (désactiver animations)
- [ ] Mode daltonien (couleurs adaptées)
- [ ] Taille de police ajustable
- [ ] Mode contraste élevé
- [ ] Support lecteur d'écran (descriptions textuelles)

---

### Version 2.0 - Fonctionnalités futures 🚀
**Statut** : 💭 En réflexion | **Date estimée** : Q4 2026

#### Idées en cours d'évaluation
- [ ] Mode multijoueur local (coopératif)
- [ ] Système de crafting (outils, abris)
- [ ] Carte de l'île à explorer
- [ ] Système météo dynamique
- [ ] Bestiaire avec comportements hardcodés
- [ ] Quêtes et objectifs secondaires
- [ ] Système de compétences et progression
- [ ] Modes de jeu alternatifs (speed run, endurance)
- [ ] Support multilingue
- [ ] Achievements/Succès débloquables

---

### Comment contribuer à la roadmap

Vous souhaitez participer à une fonctionnalité ? Voici comment :

1. **Consultez les issues GitHub** : Chaque fonctionnalité majeure a une issue dédiée
2. **Commentez votre intérêt** : Indiquez sur quelle partie vous souhaitez travailler
3. **Proposez vos idées** : Ouvrez une discussion pour de nouvelles fonctionnalités
4. **Partagez vos prototypes** : Les preuves de concept sont les bienvenues

#### Labels des issues
- `roadmap:ascii-art` - Fonctionnalités liées à l'ASCII art
- `roadmap:minigames` - Développement des mini-jeux
- `roadmap:ui` - Améliorations de l'interface
- `roadmap:future` - Idées pour versions futures

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
2. Créez une branche pour votre fonctionnalité (`git checkout -b feature/amazing_feature`)
3. Committez vos changements (`git commit -m 'Add some amazing_feature'`)
4. Poussez vers la branche (`git push origin feature/amazing_feature`)
5. Ouvrez une Pull Request

### Guidelines

- Respectez la structure du code existant
- Commentez les fonctions complexes
- Testez vos modifications sur tous les niveaux de difficulté
- Mettez à jour la documentation si nécessaire
- Suivez les conventions PEP 8 pour le code Python

## 📝 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## 👥 Auteur

- **DantesDels** - *Développeur principal* - [Lien GitHub](https://github.com/dantesdels)

## 🙏 Remerciements

- Inspiré par les jeux de survie classiques
- Merci à tous les contributeurs
- Communauté Python pour les excellentes ressources

## 📞 Support

Pour toute question ou problème :
- Ouvrez une [issue](https://github.com/dantesdels/island-survival-game/issues)
- Consultez les [discussions](https://github.com/dantesdels/island-survival-game/discussions)
- Contactez-nous par email : sebastien.delver@ynov.com

## 📊 Statistiques du projet

![GitHub stars](https://img.shields.io/github/stars/dantesdels/island-survival-game)
![GitHub forks](https://img.shields.io/github/forks/dantesdels/island-survival-game)
![GitHub issues](https://img.shields.io/github/issues/dantesdels/island-survival-game)
![GitHub license](https://img.shields.io/github/license/dantesdels/island-survival-game)

---

**Bon jeu et bonne survie ! 🏝️**

*Dernière mise à jour : Octobre 2025*
