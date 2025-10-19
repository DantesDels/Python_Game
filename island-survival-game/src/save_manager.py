import json
import os
from datetime import datetime
from player import Player
from difficulty_manager import difficulty_manager

def save_game(game):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    print(f"{game.player.name} | {game.player.days_survived} | {game.player.hunger} | {game.player.thirst} | {game.player.energy} - Sauvegarde de la partie en cours...")
    
    player = Player(
        name=game.player.name,
        hunger=game.player.hunger,
        thirst=game.player.thirst,
        energy=game.player.energy,
        days_survived=game.player.days_survived
    )

    saved_data = {
        'save_name': timestamp,
        'player': {
            'name': player.name,
            'hunger': player.hunger,
            'thirst': player.thirst,
            'energy': player.energy,
            'days_survived': player.days_survived
            },
        'game': {
            'difficulty': game.selected_difficulty
            }
        }
    with open(f'../saves/{timestamp}.json', 'w', encoding='utf-8') as save_file:
        json.dump(saved_data, save_file)
        print(f"Partie sauvegardée : {timestamp}\n")
        return saved_data
    
    
def to_save(self):
    if not os.path.exists('../saves/'):
        os.makedirs('../saves/')

    save_game(self)

def to_load(timestamp):
    with open(f'../saves/{timestamp}.json', 'r', encoding='utf-8') as save_file:
        loaded_data = json.load(save_file)
    return loaded_data