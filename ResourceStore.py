# Defines the ResourceStore Class and defines __init__ and a private dictionary is created where resource starts from 0.
class ResourceStore:
    def __init__(self):
        self.__quantities = {"food": 0, "water": 0, "oxygen": 0}

# returns none if resource is not a string or if it doesnt exist in the dictionary, stock stays unchanged. And returns the requested quantity.
    def quantity_of(self, resource):
        if type(resource) is not str or resource not in self.__quantities:
            return None
        return self.__quantities[resource]

# returns none if resource is not a str or resource doesnt exist in the dictionary, 
    def add(self, resource, amount):
        if type(resource) is not str or resource not in self.__quantities or type(amount) is not int or amount <= 0:
            return None
# then sets the new_quantity with the amount and returns it
        new_quantity = self.__quantities[resource] + amount
        self.__quantities[resource] = new_quantity
        return new_quantity
#try_consume function, first it checks if its in the dictionary and returns False for invalid input or insufficient stock.
    def try_consume(self, requirements):
        if type(requirements) is not dict:
            return False

        for resource, amount in requirements.items():
            if type(resource) is not str or resource not in self.__quantities or type(amount) is not int or amount <= 0:
                return False
            if self.__quantities[resource] < amount:
                return False
# if its valid, then it subtracts the amount consumed.
        for resource, amount in requirements.items():
            self.__quantities[resource] -= amount

        return True

    def __str__(self):
        return (f"Food: {self.__quantities['food']}, "
                f"Water: {self.__quantities['water']}, "
                f"Oxygen: {self.__quantities['oxygen']}")
