class Player:
    def __init__(self, name):
        self.name = name
        self.hunger = 0  # 0 = full, 100 = starving
        self.thirst = 0  # 0 = hydrated, 100 = dehydrated
        self.energy = 0  # 0 = exhausted, 100 = energized
        self.days_survived = 0
class Player:
    def __init__(self, name):
        self.name = name
        # starting values
        self.hunger = 20  
        self.thirst = 20  
        self.energy = 50  
        self.days_survived = 0

    def eat(self, amount):
        self.hunger = max(0, self.hunger - amount)

    def drink(self, amount):
        self.thirst = max(0, self.thirst - amount)

    def sleep(self):
        self.energy = min(100, self.energy + 50)
        self.hunger += 10
        self.thirst += 10

    def fish(self):
        # fishing reduces hunger but costs energy
        self.hunger = max(0, self.hunger - 25)
        self.energy = max(0, self.energy - 15)

    def search_water(self):
        # searching water reduces thirst but costs energy
        self.thirst = max(0, self.thirst - 30)
        self.energy = max(0, self.energy - 15)

    def explore(self):
        # simple random event: small chance to find resources or get hurt
        import random
        roll = random.randint(1, 100)
        if roll <= 10:
            # find food
            print("You found some fruits! Hunger reduced.")
            self.hunger = max(0, self.hunger - 30)
        elif roll <= 20:
            # find water
            print("You found drinking water! Thirst reduced.")
            self.thirst = max(0, self.thirst - 30)
        elif roll <= 40:
            # encounter - lose energy
            print("Dangerous encounter — you got hurt. Energy reduced.")
            self.energy = max(0, self.energy - 30)
        else:
            print("Calm exploration — nothing notable.")

    def end_day(self):
        self.days_survived += 1
        # natural deterioration per day
        self.hunger = min(100, self.hunger + 8)
        self.thirst = min(100, self.thirst + 10)
        self.energy = max(0, self.energy - 20)

    def is_alive(self):
        return self.hunger < 100 and self.thirst < 100 and self.energy > 0

    def __str__(self):
        return f"{self.name} — Hunger: {self.hunger}, Thirst: {self.thirst}, Energy: {self.energy}, Days: {self.days_survived}"