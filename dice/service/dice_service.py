from abc import ABC, abstractmethod


class DiceService(ABC):
    @abstractmethod
    def requestListResult(self):
        pass
    