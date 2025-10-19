class Player:
    def __init__(self, name, daily_mult=0.5, hunger=20, thirst=20, energy=50, days_survived=0):
        self.name = name
        # starting values
        self.daily_mult = daily_mult
        self.hunger = hunger # 0 = full, 100 = starving
        self.thirst = thirst  # 0 = hydrated, 100 = dehydrated
        self.energy = energy  # 0 = exhausted, 100 = energized
        self.days_survived = days_survived

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

    def end_day(self, growth_rate):
        self.days_survived += 1
        self.daily_mult *= (1 + growth_rate)
        # natural deterioration per day
        self.hunger = int(min(100, self.hunger + self.daily_mult))
        self.thirst = int(min(100, self.thirst + self.daily_mult))
        self.energy = int(max(0, self.energy - self.daily_mult))

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