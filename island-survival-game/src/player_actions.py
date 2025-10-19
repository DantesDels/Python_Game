from save_manager import to_save, to_load

def get_player_action():
    action = input("Choisissez une action :\n 1 - Pêcher\n 2 - Chercher de l'Eau\n 3 - Dormir\n 4 - Explorer\n\n S - Sauvegarder la Partie\n C - Charger une Partie\n Q - Quitter\n\n  Votre choix : ")
    # map french/english inputs
    action = action.strip().lower()
    map = {
        '1': 'fish', 'pêcher': 'fish', 'pecher': 'fish', 'fish': 'fish',
        '2': 'search_water', 'eau': 'search_water', 'chercher': 'search_water', 'search_water': 'search_water',
        '3': 'sleep', 'dormir': 'sleep', 'sleep': 'sleep',
        '4': 'explore', 'explorer': 'explore', 'explore': 'explore',
        's': 'save', 'sauvegarder': 'save', 'save': 'save',
        'c': 'load', 'charger': 'load', 'load': 'load',
        'q': 'exit', 'quitter': 'exit', 'exit': 'exit'
    }
    return map.get(action, action)
    
def process_action(game, action):
    if action == "fish":
        game.player.fish()
    elif action == "search_water":
        game.player.search_water()
    elif action == "sleep":
        game.player.sleep()
    elif action == "explore":
        game.player.explore()
    elif action == "save":
        to_save(game)
    elif action == "load":
        to_load()
    elif action == "exit":
        game.clear_screen()
        print("\n Merci d'avoir joué !")
        exit()
    else:
        print("Action invalide. Aucun effet pour ce tour.")