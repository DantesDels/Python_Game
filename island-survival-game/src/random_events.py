import utils

def apply_effect(player, effect):
    if effect["type"] == "hunger_increase":
        player.hunger.increase(effect["cost"])
    elif effect["type"] == "hunger_decrease":
        player.hunger.decrease(effect["cost"])

    elif effect["type"] == "thirst_increase":
        player.thirst.increase(effect["cost"])
    elif effect["type"] == "thirst_decrease":
        player.thirst.decrease(effect["cost"])

    elif effect["type"] == "energy_increase":
        player.energy.increase(effect["cost"])
    elif effect["type"] == "energy_decrease":
        player.energy.decrease(effect["cost"])

    elif effect["type"] == "player_choice":
        print("Choisissez une action :\n 1 - Chasser l'animal (diminue la faim)\n 2 - Fuir (diminue l'énergie)\n")
        choice = input("Votre choix : ")
        choice = choice.strip().lower()
        map = {
            '1': '1', 'chasser': '1', 'hunt': '1', 'h': '1',
            '2': '2', 'fuir': '2', 'run': '2', 'r': '2'
        }
        choice = map.get(choice, choice)
        if choice == "1":
            player.hunger.decrease(30)
            print("\nVous avez chassé l'animal avec succès !\n - La faim diminue de 30 -")
        elif choice == "2":
            player.energy.decrease(20)
            print("\nVous avez fui l'animal !\n - L'énergie diminue de 20 -")
        else:
            print("Choix invalide. Aucune action entreprise.")

    else:
        print("Erreur : Type d'effet inconnu.")

def trigger_random_event(game):
    data = utils.get_json_data('../res/random_events.json')
    events = data["events"]
    roll = utils.generate_random_number(1, 100)
    for event in events:
        try:
            if roll <= event["chance"]:
                print(f"\n  RANDOM EVENT :\n{event['description']}\n")
                apply_effect(game.player, event["effect"])
                break
        except Exception as e:
            utils.clear_screen()
            utils.log_error(e)