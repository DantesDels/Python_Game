import json
from constants import *
from player import Player

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
        print(f"Faim : {self.player.hunger}")
        print(f"Soif : {self.player.thirst}")
        print(f"Energie : {self.player.energy}\n")

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


    def difficulty_manager(difficulty, days_survived):
       difficulty = open('difficulty_levels.json', 'r')
       difficulty_data = json.load(difficulty)
       difficulty.close()

       days_survived = Player.self.days_survived
       
       Player.self.hunger = min(100, max(0, Player.self.hunger))
       Player.self.thirst = min(100, max(0, Player.self.thirst))
       Player.self.energy = min(0, max(100, Player.self.energy))

       if difficulty_data.get(difficulty):
           settings = difficulty_data[difficulty]
           Player.self.hunger += settings.get("hunger")
           Player.self.thirst += settings.get("thirst")
           Player.self.energy += settings.get("energy")
           
       else:
           print("Unknown difficulty level. Default settings applied.")
           settings = difficulty_data["Normal"]
           Player.self.hunger += settings.get("hunger")
           Player.self.thirst += settings.get("thirst")
           Player.self.energy += settings.get("energy")

       for days_survived in range(difficulty["days_left"]):
           days_survived += 1
           if days_survived == difficulty["days_left"]:
               break
           else:
               daily_mult_data += settings.get("daily_growth")
           pass

