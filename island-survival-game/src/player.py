from gauges import Gauge
import json

class Player:
    def __init__(self, name, difficulty="Baby", hunger=None, thirst=None, energy=None, days_survived=0):
        self.name = name
        # starting values
        initial_values = self.get_difficulty(difficulty)
        
        self.hunger = Gauge("Hunger", initial_value=hunger if hunger is not None 
                            else initial_values["hunger"], critical_value=100)
        
        self.thirst = Gauge("Thirst", initial_value=thirst if thirst is not None 
                            else initial_values["thirst"], critical_value=100)
        
        self.energy = Gauge("Energy", initial_value=energy if energy is not None 
                            else initial_values["energy"], critical_value=0)
        
        self.days_survived = days_survived

    def hunt(self, amount, energy_amount):
        self.hunger.increase(amount)
        self.energy.decrease(energy_amount)

    def sleep(self, amount, energy_amount):
        self.energy.increase(energy_amount)
        self.hunger.decrease(amount)
        self.thirst.decrease(amount)

    def fish(self, amount, energy_amount):
        # fishing reduces hunger but costs energy
        self.hunger.decrease(amount)
        self.energy.decrease(energy_amount)

    def search_water(self, amount, energy_amount):
        # searching water reduces thirst but costs energy
        self.thirst.decrease(amount)
        self.energy.decrease(energy_amount)

    def explore(self, amount):
        # simple random event: small chance to find resources or get hurt
        import random
        roll = random.randint(1, 100)
        if roll <= 10:
            # find food - reduce hunger
            print("Tu as trouvé de la nourriture ! La faim diminue.")
            self.hunger = max(0, self.hunger - amount)
        elif roll <= 20:
            # find water - reduce thirst
            print("Tu as trouvé de l'eau potable ! La soif diminue.")
            self.thirst = max(0, self.thirst - amount)
        elif roll <= 40:
            # encounter - lose energy
            print("Rencontre dangereuse — vous avez été blessé. Énergie réduite.")
            self.energy = max(0, self.energy - amount)
        else:
            print("Tu as eu la Flemme d'explorer — Rien ne s'est passé.")
            
    def get_difficulty(self, difficulty):
        with open('../res/../res/difficulty_player.json', 'r') as difficulty_player_file:
            difficulties = json.load(difficulty_player_file)
        return difficulties.get(difficulty, difficulties["Baby"])

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