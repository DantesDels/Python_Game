from constants import *
from utils import format_gauge

class Game:
 
    def __init__(self, player):
        self.player = player
        self.day = 1
        self.is_game_over = False
    def start_game(self):
        print("Bienvenue sur l'île — survivez le plus longtemps possible !\n")
        while not self.is_game_over:
            self.display_status()
            action = self.get_player_action()
            self.process_action(action)
            # end of day automatic updates
            self.player.end_day()
            self.check_game_over()
            self.day += 1
        print(f"Partie terminée après {self.player.days_survived} jours.\nEtat final : {self.player}")
              
    def display_status(self):
        print(f"Jour {self.day}")
        print("   Faim : ", format_gauge(self.player.hunger, 100))
        print("   Soif : ", format_gauge(self.player.thirst, 100))
        print("Energie : ", format_gauge(self.player.energy, 100))

    def get_player_action(self):
        action = input("Choisissez une action (pêcher, eau, dormir, explorer) : ")
        # map french/english inputs
        action = action.strip().lower()
        mapping = {
            'pêcher': 'fish', 'pecher': 'fish', 'fish': 'fish',
            'eau': 'search_water', 'chercher': 'search_water', 'search_water': 'search_water',
            'dormir': 'sleep', 'sleep': 'sleep',
            'explorer': 'explore', 'explore': 'explore'
        }
        return mapping.get(action, action)
    
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

    def reset_game(self):
        if hasattr(self.player, 'reset'):
            self.player.reset()
        self.day = 1
        self.is_game_over = False