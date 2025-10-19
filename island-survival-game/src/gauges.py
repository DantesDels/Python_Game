class Hunger:
    MAX_VALUE = 100
    MIN_VALUE = 0

    def __init__(self, initial_value=20):
        self.value = initial_value

    def increase(self, amount):
        self.value = min(self.MAX_VALUE, self.value + amount)

    def decrease(self, amount):
        self.value = max(self.MIN_VALUE, self.value - amount)

    def is_starving(self):
        return self.value >= self.MAX_VALUE
    
    
class Thirst:
    MAX_VALUE = 100
    MIN_VALUE = 0

    def __init__(self, initial_value=20):
        self.value = initial_value

    def increase(self, amount):
        self.value = min(self.MAX_VALUE, self.value + amount)

    def decrease(self, amount):
        self.value = max(self.MIN_VALUE, self.value - amount)

    def is_dehydrated(self):
        return self.value >= self.MAX_VALUE
    
    
class Energy:
    MAX_VALUE = 100
    MIN_VALUE = 0

    def __init__(self, initial_value=50):
        self.value = initial_value

    def increase(self, amount):
        self.value = min(self.MAX_VALUE, self.value + amount)

    def decrease(self, amount):
        self.value = max(self.MIN_VALUE, self.value - amount)

    def is_exhausted(self):
        return self.value <= self.MIN_VALUE