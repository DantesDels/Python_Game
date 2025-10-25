import random
from gauges import Gauge
from  utils import get_json_data
from difficulty_manager import difficulty_manager

class Player:

    def __init__(self, name, difficulty="Baby", hunger=None, thirst=None, energy=None, days_survived=0):
        self.name = name
        # starting player values
        INITIAL_VALUES = self.get_player_difficulty(difficulty)
        # world constants
        WORLD_DIFFICULTY = difficulty_manager(difficulty)
        DIFFICULTY_INCREASE = WORLD_DIFFICULTY["daily_mult"] * WORLD_DIFFICULTY["growth_rate"]
        # adjusted values based on difficulty
        self.amount_per_tour = WORLD_DIFFICULTY["amount_per_tour"] + DIFFICULTY_INCREASE
        self.energy_cost = WORLD_DIFFICULTY["energy_cost"] + DIFFICULTY_INCREASE

        self.hunger = Gauge("Hunger", initial_value=hunger if hunger is not None
                            else INITIAL_VALUES["hunger"], critical_value=100)

        self.thirst = Gauge("Thirst", initial_value=thirst if thirst is not None
                            else INITIAL_VALUES["thirst"], critical_value=100)

        self.energy = Gauge("Energy", initial_value=energy if energy is not None
                            else INITIAL_VALUES["energy"], critical_value=0)

        self.days_survived = days_survived
    
    def get_player_difficulty(self, difficulty="Baby"):
        self.get_json_data = get_json_data('../res/difficulty_player.json')
        player_difficulties = self.get_json_data
        return player_difficulties.get(difficulty, player_difficulties["Baby"])

    def hunt(self):
        self.hunger.increase(self.amount_per_tour)
        self.energy.decrease(self.energy_cost)

    def fish(self):
        self.hunger.decrease(self.amount_per_tour)
        self.energy.decrease(self.energy_cost)

    def search_water(self):
        self.thirst.decrease(self.amount_per_tour)
        self.energy.decrease(self.energy_cost)

    def sleep(self):
        self.energy.increase(self.energy_cost)
        self.hunger.decrease(self.amount_per_tour)
        self.thirst.decrease(self.amount_per_tour)

    def explore(self):
        roll = random.randint(1, 100)
        if roll <= 10:
            print("Tu as trouvé de la nourriture ! La faim diminue.")
            self.hunger = max(0, self.hunger.decrease(self.amount_per_tour))
            self.energy = max(0, self.energy.decrease(self.energy_cost))

        elif roll <= 20:
            print("Tu as trouvé de l'eau potable ! La soif diminue.")
            self.thirst = max(0, self.thirst.decrease(self.amount_per_tour))
            self.energy = max(0, self.energy.decrease(self.energy_cost))

        elif roll <= 40:
            print("Rencontre dangereuse — vous avez été blessé. Énergie réduite.")
            self.hunger = max(0, self.hunger.increase(self.amount_per_tour))
            self.thirst = max(0, self.thirst.increase(self.amount_per_tour))
            self.energy = max(0, self.energy.decrease(self.energy_cost))
        else:
            print("Tu as eu la Flemme d'explorer — Rien ne s'est passé.")

    def is_alive(self):
        return not (self.hunger.is_critical() or self.thirst.is_critical() or self.energy.is_critical())
    
    def reset(self):
        self.hunger = Gauge("Hunger", initial_value=20, critical_value=100)
        self.thirst = Gauge("Thirst", initial_value=20, critical_value=100)
        self.energy = Gauge("Energy", initial_value=50, critical_value=0)
        self.days_survived = 0
        self.daily_mult = 0.5

    def __str__(self):
        return f"{self.name} — Hunger: {self.hunger}, Thirst: {self.thirst}, Energy: {self.energy}, Days: {self.days_survived}"