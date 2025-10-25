import utils
from player import Player
from difficulty_manager import difficulty_manager
from difficulty_manager import difficulty_manager, select_difficulty
from player_actions import get_player_action, process_action

class Game:
 
    def __init__(self, player):
        self.player : Player = player
        self.day = 1
        self.is_game_over = False
        
    def start_game(self, from_load=False):
    #   utils.full_screen()
        utils.clear_screen()
        
        if not from_load:
            print("=== Jeu de Survie sur l'Île ===\n")
            print("Menu - Accès au Menu Principal\n")
            self.player.name = input("Entrez le nom de votre personnage : ")
            if self.player.name.strip().lower() == "menu":
                return utils.go_to_menu(self)
            utils.clear_screen()

            print(f"Bienvenue à toi {self.player.name} !\n")
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
            self.display_status()
            action = get_player_action()
            process_action(self, action)
            # end of day automatic updates
            self.end_day(difficulty_settings["growth_rate"])
            self.check_game_over()
            self.day += 1
        print(f"Partie terminée après {self.player.days_survived} jours.\n")
        
        if not self.is_game_over:
            print("Félicitations ! Vous avez survécu jusqu'à la fin du défi !")

    def display_status(self):
        print(f"{self.player.name} | Jour {self.day}")
        print(self.player.hunger)
        print(self.player.thirst)
        print(self.player.energy)
            
    def end_day(self, growth_rate):
        self.player.days_survived += 1
        self.daily_mult *= (1 + growth_rate)
        # natural deterioration per day
        self.player.hunger.increase(self.daily_mult)
        self.player.thirst.increase(self.daily_mult)
        self.player.energy.decrease(self.daily_mult)

    def check_game_over(self):
        if not self.player.is_alive():
            self.is_game_over = True
            print("Game Over! Vous n'avez pas survécu. \n")
            self.display_status()
            print(f"Vous avez survécu pendant {self.player.days_survived} jours.\n")
            self.reset_game()

    def clear_game(self):
        self.player.reset()
        self.day = 1
        self.is_game_over = False

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
            self.start_game()
        elif choice == "2":
            utils.quit_game(self)
        else:
            print("Choix invalide.")
            self.reset_game()