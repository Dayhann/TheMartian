from Equipment import Equipment


class Greenhouse(Equipment):
    """Grow food across successful sols, pausing during failures."""

    def __init__(self):
        super().__init__("Greenhouse")
        self.__water_per_sol = 1
        self.__food_per_harvest = 3
        self.__sols_per_harvest = 3
        self.__growth_sols = 0

    def _perform_work(self, store):
        """Use water to grow the crop and harvest when ready."""
        requirements = {"water": self.__water_per_sol}
        if not store.try_consume(requirements):
            return False

        self.__growth_sols += 1
        if self.__growth_sols >= self.__sols_per_harvest:
            store.add("food", self.__food_per_harvest)
            self.__growth_sols = 0
        return True

    def __str__(self):
        return (f"{super().__str__()}, growth: "
                f"{self.__growth_sols}/{self.__sols_per_harvest} sols")
