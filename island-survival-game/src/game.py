import os
from utils import format_gauge
from difficulty_manager import difficulty_manager
from player import Player

class Game:
 
    def __init__(self, player):
        self.player : Player = player
        self.day = 1
        self.is_game_over = False
        
    def start_game(self):
        self.clear_screen()
        print("=== Jeu de Survie sur l'Île ===\n")
        self.player.name = input("Entrez le nom de votre personnage : ")
        self.clear_screen()

        print(f"Bienvenue à toi {self.player.name} !\n")
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
        selected_difficulty = difficulty_map.get(selected_difficulty, 'Baby')
        self.selected_difficulty = selected_difficulty
        self.clear_screen()
        
        print("Bienvenue sur l'île — survivez le plus longtemps possible !\n")
        difficulty_settings = difficulty_manager(selected_difficulty)
        self.player.daily_mult = difficulty_settings["daily_mult"]
        
        while not self.is_game_over and self.day <= difficulty_settings["days_left"]:
            self.display_status()
            action = self.get_player_action()
            self.process_action(action)
            self.clear_screen()
            # end of day automatic updates
            self.player.end_day(difficulty_settings["growth_rate"])
            self.check_game_over()
            self.day += 1
        print(f"Partie terminée après {self.player.days_survived} jours.\n")
        
        if not self.is_game_over:
            print("Félicitations ! Vous avez survécu jusqu'à la fin du défi !")
              
    def display_status(self):
        print(f"{self.player.name} | Jour {self.day} | Difficulté : {self.selected_difficulty}\n")
        print("   Faim : ", format_gauge(self.player.hunger, 100))
        print("   Soif : ", format_gauge(self.player.thirst, 100))
        print("Energie : ", format_gauge(self.player.energy, 100), "\n")

    def clear_screen(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def get_player_action(self):
        action = input("Choisissez une action :\n 1 - Pêcher\n 2 - Chercher de l'Eau\n 3 - Dormir\n 4 - Explorer\n\n  Votre choix : ")
        # map french/english inputs
        action = action.strip().lower()
        map = {
            '1': 'fish', 'pêcher': 'fish', 'pecher': 'fish', 'fish': 'fish',
            '2': 'search_water', 'eau': 'search_water', 'chercher': 'search_water', 'search_water': 'search_water',
            '3': 'sleep', 'dormir': 'sleep', 'sleep': 'sleep',
            '4': 'explore', 'explorer': 'explore', 'explore': 'explore'
        }
        return map.get(action, action)
    
    def process_action(self, action):
        if action == "fish":
            self.player.fish()
        elif action == "search_water":
            self.player.search_water()
        elif action == "sleep":
            self.player.sleep()
        elif action == "explore":
            self.player.explore()
        else:
            print("Action invalide. Aucun effet pour ce tour.")

    def check_game_over(self):
        if not self.player.is_alive():
            self.is_game_over = True
            print("Game Over! Vous n'avez pas survécu. \n")
            self.display_status()
            print(f"Vous avez survécu pendant {self.player.days_survived} jours.\n")
            self.reset_game()
         

    def reset_game(self):
        print("Voulez-vous recommencer une partie ?\n 1 - Oui\n 2 - Non\n")
        choice = input("Votre choix : ")
        choice = choice.strip().lower()
        map = {
            '1': '1', 'oui': '1', 'yes': '1', 'y': '1', 'o': '1',
            '2': '2', 'non': '2', 'no': '2', 'n': '2'
        }
        choice = map.get(choice, choice)
        if choice == "1":
            self.start_game()
        elif choice == "2":
            print("Merci d'avoir joué !")
            exit()
        else:
            print("Choix invalide.")
            self.reset_game()