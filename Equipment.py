from abc import ABC, abstractmethod
#Equipment is abstract and each subclass defines _perform_work()
class Equipment(ABC):
    def __init__(self, name):
        self.__name = name
        self.__operational = True
#returns False if the operational state is broken otherwise it calls _perform_work(store) and returns its result
    def operate(self, store):
        if not self.__operational:
            return False
        return self._perform_work(store)

    @abstractmethod
    def _perform_work(self, store):
        pass
#break down and repair changes the operational states.
    def break_down(self):
        self.__operational = False

    def repair(self):
        self.__operational = True
#reports the operational state, returns True or False.
    def is_operational(self):
        return self.__operational
#displays the equipment's name and whether is it operational or broken.
    def __str__(self):
        if self.__operational:
            state = "operational"
        else:
            state = "broken"
        return f"{self.__name}: {state}"
