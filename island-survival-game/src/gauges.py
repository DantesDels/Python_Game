class Gauge:
    MAX_VALUE = 100
    MIN_VALUE = 0
    critical_value = 0

    def __init__(self, name, initial_value=20, critical_value=0):
        self.name = name
        self.value = initial_value
        self.critical_value = critical_value

    def increase(self, amount):
        self.value = int(min(self.MAX_VALUE, self.value + amount))

    def decrease(self, amount):
        self.value = int(max(self.MIN_VALUE, self.value - amount))

    def is_critical(self):
        return self.value == self.critical_value
    
    def __str__(self):
        filled_length = int(self.value / self.MAX_VALUE * 20)
        bar = '█' * filled_length + '░' * (20 - filled_length)
        return f"[{bar}] {self.value}/{self.MAX_VALUE} - {self.name}"