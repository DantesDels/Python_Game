import json
import os
from player import Player

def to_save(self):
    from datetime import datetime
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    if not os.path.exists('../saves/'):
        os.makedirs('../saves/')
    
    player_saves = input("Voulez-vous sauvegarder la partie ? (oui/non) : ")
    player_saves = player_saves.strip().lower()
      
    if player_saves in ['oui', 'o', 'yes', 'y']:
        print("Partie sauvegardée.\n")
        save_game(timestamp, self.player, self)
    elif player_saves in ['non', 'n', 'no']:
        print("Sauvegarde annulée.\n")
        return
    elif player_saves not in ['oui', 'o', 'yes', 'y', 'non', 'n', 'no']:
        print("Entrée invalide. Sauvegarde annulée.\n")
        return
    
    save_game(timestamp, self)
    print(f"Partie sauvegardée sous le nom : {timestamp}\n")


def save_game(timestamp, player, game):
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
            'difficulty': game.difficulty
            }
        }
    with open(f'../saves/{timestamp}.json', 'w', encoding='utf-8') as save_file:
        json.dump(saved_data, save_file)
        return saved_data
    

def load_game(timestamp):
    with open(f'../saves/{timestamp}.json', 'r', encoding='utf-8') as save_file:
        loaded_data = json.load(save_file)
    return loaded_data