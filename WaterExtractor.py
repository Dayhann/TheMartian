from Equipment import Equipment


class WaterExtractor(Equipment):
    """Produce three water units per successful operation."""

    def __init__(self):
        super().__init__("Water Extractor")
        self.__water_per_sol = 3

    def _perform_work(self, store):
        """Add the extracted water to the shared resource store."""
        store.add("water", self.__water_per_sol)
        return True
