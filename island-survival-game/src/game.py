from utils import format_gauge
from difficulty_manager import difficulty_manager
from player import Player

class Game:
 
    def __init__(self, player):
        self.player : Player = player
        self.day = 1
        self.is_game_over = False
        
    def start_game(self):
        self.player.name = input("Entrez le nom de votre personnage : ")
        selected_difficulty = input("Selectionnez une difficulté : \n1 - Baby \n2 - Easy \n3 - Medium \n4 - Hard \n5 - Nightmare \nVotre choix : ")
        selected_difficulty = selected_difficulty.strip().lower()
        difficulty_map = {
            '1': 'Baby', 'baby': 'Baby', 'Baby': 'Baby', 'BABY': 'Baby',
            '2': 'Easy', 'easy': 'Easy', 'Easy': 'Easy', 'EASY': 'Easy',
            '3': 'Medium', 'medium': 'Medium', 'Medium': 'Medium', 'MEDIUM': 'Medium',
            '4': 'Hard', 'hard': 'Hard', 'Hard': 'Hard', 'HARD': 'Hard',
            '5': 'Nightmare', 'nightmare': 'Nightmare', 'Nightmare': 'Nightmare', 'NIGHTMARE': 'Nightmare'
        }
        selected_difficulty = difficulty_map.get(selected_difficulty, 'Baby')
        print("Bienvenue sur l'île — survivez le plus longtemps possible !\n")
        difficulty_settings = difficulty_manager(selected_difficulty)
        self.player.daily_mult = difficulty_settings["daily_mult"]
        
        while not self.is_game_over and self.day <= difficulty_settings["days_left"]:
            self.display_status()
            action = self.get_player_action()
            self.process_action(action)
            # end of day automatic updates
            self.player.end_day(difficulty_settings["growth_rate"])
            self.check_game_over()
            self.day += 1
        print(f"Partie terminée après {self.player.days_survived} jours.\n")
        
        if not self.is_game_over:
            print("Félicitations ! Vous avez survécu jusqu'à la fin du défi !")
              
    def display_status(self):
        print(f"{self.player.name} | Jour {self.day}")
        print("   Faim : ", format_gauge(self.player.hunger, 100))
        print("   Soif : ", format_gauge(self.player.thirst, 100))
        print("Energie : ", format_gauge(self.player.energy, 100))

    def get_player_action(self):
        action = input("Choisissez une action :\n 1 - Pêcher\n 2 - Chercher de l'Eau\n 3 - Dormir\n 4 - Explorer\n Votre choix : ")
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
            print("Game Over! Vous n'avez pas survécu.")
            self.display_status()

    def reset_game(self):
        if hasattr(self.player, 'reset'):
            self.player.reset()
        self.day = 1
        self.is_game_over = False