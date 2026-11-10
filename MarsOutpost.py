from Astronaut import Astronaut
from Equipment import Equipment
from MissionLog import MissionLog
from ResourceStore import ResourceStore


class MarsOutpost:
    """Coordinate the astronaut, supplies and daily equipment work."""

    DEFAULT_TARGET_SOLS = 10

    def __init__(self, astronaut, target_sols=10):
        self.__astronaut = astronaut
        self.__target_sols = self.DEFAULT_TARGET_SOLS
        if type(target_sols) is int and target_sols > 0:
            self.__target_sols = target_sols

        self.__sols_completed = 0
        self.__status = "RUNNING"
        self.__store = ResourceStore()
        self.__equipment = []
        self.__log = MissionLog()

    def add_supplies(self, resource, amount):
        """Load initial supplies and return the new quantity."""
        if self.__sols_completed > 0 or self.is_finished():
            return None
        return self.__store.add(resource, amount)

    def quantity_of(self, resource):
        """Look up stock without exposing the inventory dictionary."""
        return self.__store.quantity_of(resource)

    def add_equipment(self, item):
        """Attach an equipment item once, before the mission starts."""
        if self.__sols_completed > 0 or self.is_finished():
            return False
        if not isinstance(item, Equipment) or item in self.__equipment:
            return False
        self.__equipment.append(item)
        return True

    def advance_sol(self):
        """Complete a sol and prepare supplies for the next one."""
        if self.is_finished():
            return self.__status

        attempted_sol = self.__sols_completed + 1
        if not isinstance(self.__astronaut, Astronaut):
            self.__status = "FAILED"
            self.__log.record(
                f"Sol {attempted_sol} failed: no valid astronaut."
            )
            return self.__status

        if not self.__astronaut.consume_daily_supplies(self.__store):
            self.__status = "FAILED"
            self.__log.record(
                f"Sol {attempted_sol} failed: insufficient daily supplies."
            )
            return self.__status

        self.__sols_completed += 1
        self.__log.record(f"Sol {self.__sols_completed} completed.")
        if self.__sols_completed >= self.__target_sols:
            self.__status = "SUCCEEDED"
            self.__log.record(
                f"Mission succeeded after {self.__sols_completed} sols."
            )
            return self.__status

        for item in self.__equipment:
            if item.operate(self.__store):
                result = "succeeded"
            else:
                result = "failed"
            self.__log.record(
                f"Sol {self.__sols_completed}: {item}; work {result}."
            )
        return self.__status

    def is_finished(self):
        return self.__status != "RUNNING"

    def get_broken_equipment(self):
        """Return a new list containing references to broken items."""
        return [item for item in self.__equipment
                if not item.is_operational()]

    def get_log_entries(self, keyword=""):
        return self.__log.find_entries(keyword)

    def status_report(self):
        """Return mission progress, stock and equipment details."""
        lines = [
            f"Mission status: {self.__status}",
            f"Sols completed: {self.__sols_completed}/{self.__target_sols}",
            str(self.__astronaut),
            str(self.__store),
            "Equipment:"
        ]
        if not self.__equipment:
            lines.append("  No equipment attached.")
        for item in self.__equipment:
            lines.append(f"  {item}")
        return "\n".join(lines)

    def get_sols_completed(self):
        return self.__sols_completed

    def get_target_sols(self):
        return self.__target_sols

    def get_status(self):
        return self.__status

    sols_completed = property(get_sols_completed)
    target_sols = property(get_target_sols)
    status = property(get_status)
