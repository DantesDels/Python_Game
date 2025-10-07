# Python_Game
A Python Game 


# Description
Jeu de survie,
Gestion de ressources (vitales),
Choix stratégiques,
sur plusieurs jours, 

Plusieurs jauges :
 Faim (0 = rassasié, 100 = affamé -> game over).
 Soif (0 = hydraté, 100 = déshydraté -> game over).
 Énergie (0 = épuisé -> game over).

Jour :
- x1 action par jour :
 Pêcher -> - Faime / - Energie
 Chercher de l’eau -> - Soif / - Energie
 Dormir -> + Énergie / + Soif & Faim
 Explorer -> événement aléatoire (parfois +++, parfois ---).
- Jauges évolutives,
- Events aléatoires :
o    Pluie -> réduit la soif.
o    Rencontre animale -> fuir ou chasse.
o    Découverte de fruit/ressource.

End : 
-> Jauge valeur CRITIQUE
-> Jour final atteint (ex : 30 jours).

Spécificités :
- CLI
- Système de Jours/Tours
- Affichage Jauges
- Update Jauges selon actions/events
- Gestion Game Over / Victoire
- Gestion de Sauvegarde/Chargement (JSON)


# Présentation
Ce jeu est un jeu de survie textuel où le joueur doit gérer ses ressources pour survivre le plus longtemps possible dans un environnement hostile. Le joueur doit prendre des décisions stratégiques chaque jour pour maintenir ses jauges de faim, de soif et d'énergie à des niveaux acceptables.


# Règles du jeu
1. Le joueur commence avec des jauges de faim, de soif et d'énergie à des niveaux initiaux.
2. Chaque jour, le joueur peut effectuer une action parmi les suivantes :
   - Pêcher
   - Chercher de l'eau
   - Dormir
   - Explorer
3. Les actions ont des conséquences sur les jauges du joueur.
4. Si une jauge atteint 100, le joueur perd la partie.
5. Le jeu se termine lorsque le joueur atteint un certain nombre de jours ou que ses jauges atteignent des niveaux critiques.


# Installation
1. Clonez le dépôt
2. Installez les dépendances
3. Lancez le jeu


# Gestion de Sauvegarde/Chargement
Le jeu utilise des fichiers JSON pour sauvegarder et charger l'état du jeu. Le joueur peut sauvegarder sa progression à tout moment et reprendre plus tard.

## Exemple de sauvegarde
(iso date format = file_name)
```json 
{
  "player_name": "Survivant",
  "day": 5,
  "hunger": 30,
  "thirst": 40,
  "energy": 50
}
```
## Charger une sauvegarde
Le joueur peut charger une sauvegarde en sélectionnant l'option de chargement dans le menu principal. Le jeu lira le fichier JSON et restaurera l'état du jeu à partir des données sauvegardées.
```
python3 game.py file_name.json
```

# Gestion de la Difficulté
- Plus les jours passent, plus la difficulté s'élève.
- Difficulté gérées par des multiplicateurs
- Facilement réglable


# BONUS
- Ajouter des niveaux de difficulté (facile, moyen, difficile) qui affectent la vitesse à laquelle les jauges diminuent.
- Ajouter des événements aléatoires plus variés et complexes.
- Ajouter un système d'inventaire pour gérer les ressources collectées.


