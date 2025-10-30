import utils
import main_menu
from player import Player
from difficulty_manager import difficulty_manager
from difficulty_manager import difficulty_manager, select_difficulty
from player_actions import get_player_action, process_action
import random_events

class Game:
 
    def __init__(self, player):
        self.player : Player = player
        self.day = 1
        self.is_game_over = False
        
    def start(self, from_load=False):
        utils.clear_screen()
        
        if not from_load:
            print("=== Jeu de Survie sur l'Île ===\n")
            print("Menu - Accès au Menu Principal\n")
            self.player.name = input("Entrez le nom de votre personnage : ")
            if self.player.name.strip().lower() == "menu":
                return main_menu.display_main_menu(self)

            print(f"\nBienvenue à toi {self.player.name} !\n")
            selected_difficulty = select_difficulty()
            self.selected_difficulty = selected_difficulty
            utils.clear_screen()
            
            print("Bienvenue sur l'île — survivez le plus longtemps possible !\n")
            difficulty_settings = difficulty_manager(selected_difficulty)
            self.daily_mult = difficulty_settings["daily_mult"]
        else:
            difficulty_settings = difficulty_manager(self.selected_difficulty)
            self.daily_mult = difficulty_settings["daily_mult"]
            self.day = self.player.days_survived
            for i in range(1, self.player.days_survived + 1):
                self.daily_mult *= (1 + difficulty_settings["growth_rate"])
            print(f"Chargement de la partie...\n")
        
        while not self.is_game_over and self.day <= difficulty_settings["days_left"]:
            print(f"--- Jour {self.day} ---\n")
            self.display_status()
            action = get_player_action()
            process_action(self, action)
            # end of day automatic updates
            self.end_day(difficulty_settings["growth_rate"])
            random_events.trigger_random_event(self)
            print(f"Jour {self.day} terminé.\n")
            self.day += 1
            self.check_game_over()
            input("Appuyez sur une touche pour continuer...\n")
            utils.clear_screen()
        print(f"Partie terminée après {self.player.days_survived} jours.\n")
        
        if not self.is_game_over:
            print("Félicitations ! Vous avez survécu jusqu'à la fin du défi !")
            input("Appuyez sur une touche pour continuer...")

    def display_status(self):
        print(f"{self.player.name}\n")
        print(self.player.hunger)
        print(self.player.thirst)
        print(self.player.energy)
            
    def end_day(self, growth_rate):
        self.player.days_survived += 1
        self.daily_mult *= (0.5 + growth_rate)
        # natural deterioration per day
        self.player.hunger.increase(self.daily_mult)
        self.player.thirst.increase(self.daily_mult)
        self.player.energy.decrease(self.daily_mult)

    def check_game_over(self):
        if not self.player.is_alive():
            self.is_game_over = True
            print("- GAME OVER -\n")
            self.display_status()
            print(f"\nCAUSE  : {self.player.cause_of_death()}\nVous avez survécu pendant {self.player.days_survived} jours.\n")
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
            self.clear_game()
            self.start()
        elif choice == "2":
            utils.quit_game(self)
        else:
            utils.clear_screen()
            print("Choix invalide.")
            self.reset_game()

    def clear_game(self):
        self.player.reset()
        self.day = 1
        self.is_game_over = False