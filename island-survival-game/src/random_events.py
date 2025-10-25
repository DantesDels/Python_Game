import random
import utils

def apply_effect(player, effect):
    if effect["type"] == "hunger_increase":
        player.hunger.increase(effect["magnitude"])
    elif effect["type"] == "hunger_decrease":
        player.hunger.decrease(effect["magnitude"])

    elif effect["type"] == "thirst_increase":
        player.thirst.increase(effect["magnitude"])
    elif effect["type"] == "thirst_decrease":
        player.thirst.decrease(effect["magnitude"])

    elif effect["type"] == "energy_increase":
        player.energy.increase(effect["magnitude"])
    elif effect["type"] == "energy_decrease":
        player.energy.decrease(effect["magnitude"])

def trigger_random_event(game):
    events = utils.get_json_data('../res/random_events.json')
    roll = utils.generate_random_number(1, 100)
    for event in events:
        try:
            if roll <= event["chance"]:
                print(f"Événement aléatoire : {event['description']}")
                apply_effect(game.player, event["effect"])
                break
        except Exception as e:
            utils.clear_screen()
            utils.log_error(e)