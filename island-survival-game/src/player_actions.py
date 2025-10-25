from main_menu import display_main_menu

def get_player_action():
    action = input("Choisissez une action :\n 1 - Chasser\n 2 - Pêcher\n 3 - Chercher de l'Eau\n 4 - Dormir\n 5 - Explorer\n\n M - Menu Principal\n\n  Votre choix : ")
    # map french/english inputs
    action = action.strip().lower()
    map = {
        '1': 'hunt', 'chasser': 'hunt', 'hunt': 'hunt',
        '2': 'fish', 'pêcher': 'fish', 'pecher': 'fish', 'fish': 'fish',
        '3': 'search_water', 'eau': 'search_water', 'chercher': 'search_water', 'search_water': 'search_water',
        '4': 'sleep', 'dormir': 'sleep', 'sleep': 'sleep',
        '5': 'explore', 'explorer': 'explore', 'explore': 'explore',
        'm': 'menu', 'menu': 'menu'
    }
    return map.get(action, action)
    
def process_action(game, action):
    if action == "hunt":
        game.player.hunt()
    elif action == "fish":
        game.player.fish()
    elif action == "search_water":
        game.player.search_water()
    elif action == "sleep":
        game.player.sleep()
    elif action == "explore":
        game.player.explore()

    elif action == "menu":
        display_main_menu(game)

    else:
        print("Action invalide. Aucun effet pour ce tour.")