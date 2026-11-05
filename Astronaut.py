# Astronaut class with three constants that are needed per sol, then the constructor receives the astronaut's name and saves it as the private name.
class Astronaut:

    FOOD_PER_SOL = 1
    WATER_PER_SOL = 1
    OXYGEN_PER_SOL = 1

    def __init__(self, name):
        self.__name = name

# requirements is a temporary dict inside this method, the dict is passed to store.try_consume()

    def consume_daily_supplies(self, store):
        requirements = {
            "food": self.FOOD_PER_SOL,
            "water": self.WATER_PER_SOL,
            "oxygen": self.OXYGEN_PER_SOL
        }
        return store.try_consume(requirements)

    def __str__(self):
        return f"Astronaut: {self.__name}"
