from Equipment import Equipment


class Rover(Equipment):
    """Survey new terrain using a battery stored within the rover."""

    def __init__(self):
        super().__init__("Rover")
        self.__battery_capacity = 3
        self.__battery_charge = self.__battery_capacity
        self.__distance_per_sol = 2
        self.__distance_explored = 0

    def _perform_work(self, store):
        """Spend charge on surveying without using shared supplies."""
        if self.__battery_charge == 0:
            return False

        self.__battery_charge -= 1
        self.__distance_explored += self.__distance_per_sol
        return True

    def recharge(self):
        """Restore full charge without changing distance or repairs."""
        self.__battery_charge = self.__battery_capacity

    def get_distance_explored(self):
        return self.__distance_explored

    def __str__(self):
        return (f"{super().__str__()}, battery: "
                f"{self.__battery_charge}/{self.__battery_capacity}, "
                f"explored: {self.__distance_explored} km")
