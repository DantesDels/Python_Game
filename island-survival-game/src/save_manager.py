import json

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
            'day': game.day,
            'difficulty': game.difficulty
            }
        }
    with open('save_file.json', 'w') as save_file:
        json.dump(saved_data, save_file)
    print("Game saved successfully!")
    
def load_game():
    with open('save_file.json', 'r') as save_file:
        loaded_data = json.load(save_file)
    print("Game loaded successfully!")
    return loaded_data