from abc import ABC, abstractmethod


class SystemQueueRepository(ABC):
    @abstractmethod
    def createEssential(self):
        pass
