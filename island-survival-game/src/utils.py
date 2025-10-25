import random
import os
import json
from main_menu import display_main_menu


def generate_random_number(min_value, max_value):
    return random.randint(min_value, max_value)

def validate_input(user_input, valid_options):
    return user_input in valid_options

def clear_screen():
    if os.name == 'nt':
        os.system('cls') # Windows
    else:
        os.system('clear') # Unix/Linux/MacOS

def get_json_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        json_file.close() # not obligatory due to 'with' statement, and context manager
    return data

def go_to_menu(self):
    menu_input = input("Voulez-vous retourner au menu principal ? (o/n) : ")
    if menu_input.strip().lower() in ['o', 'oui', 'y', 'yes']:
        display_main_menu()
    elif menu_input.strip().lower() in ['n', 'non', 'no']:
        self.clear_screen()
        print("Retour au jeu...")
    else:
        self.clear_screen()
        print("Choix invalide. Veuillez réessayer.")
        self.go_to_menu()