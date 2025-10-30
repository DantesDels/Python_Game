from main_menu import display_main_menu

def get_player_action():
    print("\nActions Disponibles :\n    1. Chasser\n    2. Pêcher\n    3. Chercher de l'Eau\n    4. Dormir\n    5. Explorer\n\n    M. Menu Principal")
    action = input("\n  Votre choix : ")
    if action.isspace():
        action = "Bouh le Nul ! Il s'est foiré"
        return action
    action = action.strip().lower()
    map = {
        '1': 'Chasser', 'chasser': 'Chasser', 'hunt': 'Chasser',
        '2': 'Pêcher', 'pêcher': 'Pêcher', 'pecher': 'Pêcher', 'fish': 'Pêcher',
        '3': "Chercher de l'Eau", 'eau': "Chercher de l'Eau", 'chercher': "Chercher de l'Eau", 'search_water': "Chercher de l'Eau",
        '4': 'Dormir', 'dormir': 'Dormir', 'sleep': 'Dormir',
        '5': 'Explorer', 'explorer': 'Explorer', 'explore': 'Explorer',
        'm': 'Menu Principal', 'menu': 'Menu Principal', 'menu principal': 'Menu Principal', 'main menu': 'Menu Principal'
    }
    if action in map:
        action = map[action]
    elif action == '':
        action = "Rien"
        print("\nAucune action saisie. Veuillez réessayer.")
    elif action not in map and not action == '':
        print("\nAction invalide. Veuillez réessayer.")
    return map.get(action, action)
    
def process_action(game, action):
    print(f"  ACTION REALISEE: {action}")
    if action == "Chasser":
        game.player.hunt()
    elif action == "Pêcher":
        game.player.fish()
    elif action == "Chercher de l'Eau":
        game.player.search_water()
    elif action == "Dormir":
        game.player.sleep()
    elif action == "Explorer":
        game.player.explore()

    elif action == "Menu Principal":
        display_main_menu(game)

    elif action == "Bouh le Nul ! Il s'est foiré":
        print("HAHAHAHAHAHAHA! Tu as foiré ton action en beauté ! Bravo champion !")
    elif action == "Rien":
        print("Aucun effet pour ce tour.")