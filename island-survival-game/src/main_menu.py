import utils
from save_manager import to_save, to_load

def display_main_menu(game):
    utils.clear_screen()
    print(" === MENU PRINCIPAL ===\n")
    print("  1. Nouvelle Partie \n")
    print("  2. Continuer \n")
    print("  3. Sauvegarder la Partie \n")
    print("  4. Charger une Partie \n")
    print("  5. Quitter \n\n")

    choice = input("Sélectionnez une option : ")
    choice = choice.strip().lower()
    map = {
        '1': '1', 'nouvelle partie': '1', 'new game': '1', 'n': '1',
        '2': '2', 'continuer': '2', 'continue': '2', 'c': '2',
        '3': '3', 'sauvegarder': '3', 'save': '3', 's': '3',
        '4': '4', 'charger': '4', 'load': '4', 'l': '4',
        '5': '5', 'quitter': '5', 'quit': '5', 'q': '5'
    }
    choice = map.get(choice, choice)
    if choice not in ['1', '2', '3', '4', '5']:
        print("Choix invalide. Veuillez réessayer.\n")
        return display_main_menu(game)
    elif choice == '1':
        print("Démarrage d'une nouvelle partie...\n")
        game.reset_game()
    elif choice == '2':
        print("Reprise de la dernière partie sauvegardée...\n")
        to_load(game, latest=True)
    elif choice == '3':
        print("Sauvegarde de la partie en cours...\n")
        to_save(game)
    elif choice == '4':
        print("Chargement d'une partie sauvegardée...\n")
        to_load(game)
    elif choice == '5':
        utils.quit_game(game)
    return choice
