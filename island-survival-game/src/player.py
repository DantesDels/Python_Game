from gauges import Gauge
import json

class Player:
    def __init__(self, name, difficulty="Baby"):
        self.name = name
        # starting values
        initial_values = self.get_difficulty(difficulty)
        self.hunger = Gauge("Hunger", initial_value=initial_values["hunger"], critical_value=100)
        self.thirst = Gauge("Thirst", initial_value=initial_values["thirst"], critical_value=100)
        self.energy = Gauge("Energy", initial_value=initial_values["energy"], critical_value=0)
        self.days_survived = 0

    def eat(self, amount):
        self.hunger.increase(amount)

    def drink(self, amount):
        self.thirst.increase(amount)

    def sleep(self):
        self.energy.increase(50)
        self.hunger.decrease(10)
        self.thirst.decrease(10)

    def fish(self):
        # fishing reduces hunger but costs energy
        self.hunger.decrease(25)
        self.energy.decrease(15)

    def search_water(self):
        # searching water reduces thirst but costs energy
        self.thirst.decrease(30)
        self.energy.decrease(15)

    def explore(self):
        # simple random event: small chance to find resources or get hurt
        import random
        roll = random.randint(1, 100)
        if roll <= 10:
            # find food
            print("Tu as trouvé de la nourriture ! La faim diminue.")
            self.hunger = max(0, self.hunger - 30)
        elif roll <= 20:
            # find water
            print("Tu as trouvé de l'eau potable ! La soif diminue.")
            self.thirst = max(0, self.thirst - 30)
        elif roll <= 40:
            # encounter - lose energy
            print("Rencontre dangereuse — vous avez été blessé. Énergie réduite.")
            self.energy = max(0, self.energy + 30)
        else:
            print("Calm exploration — nothing notable.")
            
    def get_difficulty(self, difficulty):
        with open('difficulty_player.json', 'r') as difficulty_player_file:
            difficulties = json.load(difficulty_player_file)
        return difficulties.get(difficulty, difficulties["Baby"])

    def is_alive(self):
        return self.hunger < 100 and self.thirst < 100 and self.energy > 0
    
    def reset(self):
        self.hunger = 20
        self.thirst = 20
        self.energy = 50
        self.days_survived = 0
        self.daily_mult = 0.5

    def __str__(self):
        return f"{self.name} — Hunger: {self.hunger}, Thirst: {self.thirst}, Energy: {self.energy}, Days: {self.days_survived}"