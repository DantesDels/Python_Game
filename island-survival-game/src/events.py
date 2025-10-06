import random
from constants import EVENT_PROBABILITIES

class Event:
    def __init__(self, description, effect):
        self.description = description
        self.effect = effect

def generate_random_event():
    pass

def handle_event(event):
    if event == "rain":
        return Event("It starts to rain, reducing your thirst.", {"thirst": -20})
    elif event == "animal_encounter":
        return Event("You encounter a wild animal. You can choose to flee or hunt.", {"energy": -10})
    elif event == "resource_discovery":
        return Event("You discover a hidden stash of fruits!", {"hunger": -15})
    return None

def apply_event_effect(player, event):
    if event.effect:
        pass