from player import Player
import json
import os

def difficulty_manager(difficulty_level):
    difficulty = open('../res/difficulty_level.json', 'r', encoding='utf-8')
    difficulty_data = json.load(difficulty)
    difficulty.close()
    return difficulty_data.get(difficulty_level, difficulty_data["Baby"])

def select_difficulty(self):
    selected_difficulty = input("Selectionnez une difficulté :\n 1 - Baby\n 2 - Easy\n 3 - Medium\n 4 - Hard\n 5 - Hardcore\n 6 - Nightmare\n\n  Votre choix : ")
    selected_difficulty = selected_difficulty.strip().lower()
    difficulty_map = {
        '1': 'Baby', 'baby': 'Baby', 'Baby': 'Baby',
        '2': 'Easy', 'easy': 'Easy', 'Easy': 'Easy',
        '3': 'Medium', 'medium': 'Medium', 'Medium': 'Medium',
        '4': 'Difficult', 'difficult': 'Difficult', 'Difficult': 'Difficult',
        '5': 'Hardcore', 'hardcore': 'Hardcore', 'Hardcore': 'Hardcore',
        '6': 'Nightmare', 'nightmare': 'Nightmare', 'Nightmare': 'Nightmare'
        }
        
    while selected_difficulty not in difficulty_map:
        self.clear_screen()
        print("Difficulté invalide. Réessayer !\n")
        selected_difficulty = input("Selectionnez une difficulté :\n 1 - Baby\n 2 - Easy\n 3 - Medium\n 4 - Hard\n 5 - Hardcore\n 6 - Nightmare\n\n  Votre choix : ")
        selected_difficulty = selected_difficulty.strip().lower()

    selected_difficulty = difficulty_map.get(selected_difficulty, 'Baby')
    self.selected_difficulty = selected_difficulty