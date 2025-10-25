import utils
import json
import os
import re
import main_menu
import player
from datetime import datetime


SAVES_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'saves'))
TIMESTAMP_PATTERN = re.compile(r'^\d{8}_\d{6}\.json$')  # 20251019_142530.json

def ensure_saves_dir():
    if not os.path.exists(SAVES_DIR):
        os.makedirs(SAVES_DIR, exist_ok=True)

def to_save(game):
    utils.clear_screen()
    ensure_saves_dir()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{timestamp}.json"
    filepath = os.path.join(SAVES_DIR, filename)

    print(f"Partie actuelle :\n\nJoueur : {game.player.name}\nJours survécus : {game.player.days_survived}\n{game.player.hunger}\n{game.player.thirst}\n{game.player.energy}\n\n")

    player = game.player
    
    saved_data = {
        'save_name': timestamp,
        'player': {
            'name': player.name,
            'hunger': player.hunger.value,
            'thirst': player.thirst.value,
            'energy': player.energy.value,
            'days_survived': player.days_survived
        },
        'game': {
            'difficulty': getattr(game, 'selected_difficulty', None)
        }
    }
 
    with open(filepath, 'w', encoding='utf-8') as save_file:
        json.dump(saved_data, save_file)
        
    print(f"Partie sauvegardée : {timestamp}\n\n")
    print(f"Appuyez sur une touche pour revenir au Menu Principal...")
    input()
    return main_menu.display_main_menu(game)

def to_load(game):
    ensure_saves_dir()
    save_files = [f for f in os.listdir(SAVES_DIR) if TIMESTAMP_PATTERN.match(f)]
    if not save_files:
        print("Aucune sauvegarde trouvée.")
        input("\nAppuyez sur une touche pour revenir au menu principal...")
        return main_menu.display_main_menu(game)

    save_files.sort(reverse=True) # latest save comes first
    
    saves = []
    for save_file in save_files:
        with open(os.path.join(SAVES_DIR, save_file), 'r', encoding='utf-8') as save_game_file:
            save_data = json.load(save_game_file)
            saves.append(save_data)

    print("Liste des sauvegardes disponibles :\n")
    for i, (save_data) in enumerate(saves, start=1):
        player_dict = save_data['player']
        print(f"{i}. {save_data['save_name']} - {player_dict['name']} | Jours {player_dict['days_survived']} | Difficulté : {save_data['game']['difficulty']} | Faim: {player_dict['hunger']} / Soif: {player_dict['thirst']} / Énergie: {player_dict['energy']}")
        
    print(f"\n R - Retour au menu principal\n")
    choice = input("Entrez le numéro de la sauvegarde à charger : ")
    if choice.strip().lower() == 'r':
        print("Retour au menu principal...\n")
        return main_menu.display_main_menu(game)
    elif not choice.isdigit() or int(choice) < 1 or int(choice) > len(saves):
        print("Choix invalide. Aucune sauvegarde chargée.")
        return None
    else :
        selected_save = saves[int(choice) - 1]
        print(f"Sauvegarde chargée : {selected_save['save_name']}\n")
        player_data = selected_save['player']
        game.player = player.Player(
            name=player_data['name'],
            difficulty=selected_save['game']['difficulty'],
            hunger=player_data['hunger'],
            thirst=player_data['thirst'],
            energy=player_data['energy'],
            days_survived=player_data['days_survived']
        )
        game.selected_difficulty = selected_save['game']['difficulty']
        game.start_game(from_load=True)