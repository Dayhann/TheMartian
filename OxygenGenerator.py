from Equipment import Equipment


class OxygenGenerator(Equipment):
    """Produce oxygen from water using the shared equipment controls."""

    def __init__(self):
        super().__init__("Oxygen Generator")
        self.__water_per_sol = 1
        self.__oxygen_per_sol = 2

    def _perform_work(self, store):
        """Use the required water before adding oxygen."""
        requirements = {"water": self.__water_per_sol}
        if not store.try_consume(requirements):
            return False

        store.add("oxygen", self.__oxygen_per_sol)
        return True
