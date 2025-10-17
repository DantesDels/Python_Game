from player import Player
import json

def difficulty_manager(difficulty_level):
    difficulty = open('../res/difficulty_level.json', 'r', encoding='utf-8')
    difficulty_data = json.load(difficulty)
    difficulty.close()
    return difficulty_data.get(difficulty_level, difficulty_data["Baby"])
 