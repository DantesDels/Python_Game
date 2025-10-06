import json
import os

def save_game(state, filename):
    with open(filename, 'w') as f:
        json.dump(state, f)

def load_game(filename):
    if not os.path.exists(filename):
        return None
    with open(filename, 'r') as f:
        return json.load(f)