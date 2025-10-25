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
        action = "\nTu as chassé avec succès !\n - La faim diminue -"
        self.hunger.decrease(self.amount_per_tour)
        self.energy.decrease(self.energy_cost)
        return print(action)

    def fish(self):
        action = "\nTu as pêché avec succès !\n - La faim diminue -"
        self.hunger.decrease(self.amount_per_tour)
        self.energy.decrease(self.energy_cost)
        return print(action)

    def search_water(self):
        action = "\nTu as cherché de l'eau avec succès !\n - La soif diminue -"
        self.thirst.decrease(self.amount_per_tour)
        self.energy.decrease(self.energy_cost)
        return print(action)

    def sleep(self):
        action = "\nTu as bien dormi !\n - L'énergie augmente -"
        self.energy.increase(self.energy_cost)
        self.hunger.decrease(self.amount_per_tour)
        self.thirst.decrease(self.amount_per_tour)
        return print(action)

    def explore(self):
        roll = random.randint(1, 100)
        print(f"\nExploration roll: {roll}")
        if roll <= 10:
            action = "Tu as trouvé de la nourriture !\n - La faim diminue -"
            self.hunger.decrease(self.amount_per_tour)
            self.energy.decrease(self.energy_cost)

        elif roll <= 20:
            action = "Tu as trouvé de l'eau potable !\n - La soif diminue -"
            self.thirst.decrease(self.amount_per_tour)
            self.energy.decrease(self.energy_cost)

        elif roll <= 40:
            action = "Rencontre dangereuse — vous avez été blessé !\n - Énergie réduite -"
            self.hunger.increase(self.amount_per_tour)
            self.thirst.increase(self.amount_per_tour)
            self.energy.decrease(self.energy_cost)
        else:
            action = "Tu as eu la Flemme d'explorer — Rien ne s'est passé."
        return print(action)

    def is_alive(self):
        return not (self.hunger.is_critical() or self.thirst.is_critical() or self.energy.is_critical())
    
    def cause_of_death(self):
        if self.hunger.is_critical():
            return "Mort de faim"
        elif self.thirst.is_critical():
            return "Mort de soif"
        elif self.energy.is_critical():
            return "Mort d'épuisement"
        return "Inconnu"
    
    def reset(self):
        self.hunger = Gauge("Hunger", initial_value=20, critical_value=100)
        self.thirst = Gauge("Thirst", initial_value=20, critical_value=100)
        self.energy = Gauge("Energy", initial_value=50, critical_value=0)
        self.days_survived = 0
        self.daily_mult = 0.5

    def __str__(self):
        return f"{self.name} — Hunger: {self.hunger}, Thirst: {self.thirst}, Energy: {self.energy}, Days: {self.days_survived}"