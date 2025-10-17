from utils import format_gauge
from difficulty_manager import difficulty_manager
from player import Player

class Game:
 
    def __init__(self, player):
        self.player : Player = player
        self.day = 1
        self.is_game_over = False
        
    def start_game(self):
        print("Bienvenue sur l'île — survivez le plus longtemps possible !\n")
        difficulty_settings = difficulty_manager("Baby")
        self.player.daily_mult = difficulty_settings["daily_mult"]
        
        while not self.is_game_over and self.day <= difficulty_settings["days_left"]:
            self.display_status()
            action = self.get_player_action()
            self.process_action(action, difficulty_settings)
            # end of day automatic updates
            self.player.end_day(difficulty_settings["growth_rate"])
            self.check_game_over()
            self.day += 1
        print(f"Partie terminée après {self.player.days_survived} jours.\n")
        
        if not self.is_game_over:
            print("Félicitations ! Vous avez survécu jusqu'à la fin du défi !")
              
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
    
    def process_action(self, action, difficulty_settings):
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