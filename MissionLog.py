class MissionLog:
    """Keep mission messages in order and provide keyword searches."""

    def __init__(self):
        self.__entries = []

    def record(self, message):
        """Append a nonempty message and return success."""
        if type(message) is not str or not message.strip():
            return False
        self.__entries.append(message)
        return True

    def find_entries(self, keyword):
        """Return a new list of messages containing the keyword."""
        if type(keyword) is not str:
            return []
        return [entry for entry in self.__entries if keyword in entry]

    def __str__(self):
        if not self.__entries:
            return "No mission events recorded."
        return "\n".join(self.__entries)
