from player import Player
import json
import os

def load_json_filename(filename):
    base = os.path.dirname(__file__)
    path = os.path.join(base, '..', 'res', filename)
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def difficulty_manager(difficulty_level, difficulty_player):
    level_difficulty_data = load_json_filename('difficulty_level.json')
    player_difficulty_data = load_json_filename('difficulty_player.json')
    return player_difficulty_data.get(difficulty_player, player_difficulty_data.get("Baby"))

# Python peut return des tuples.
