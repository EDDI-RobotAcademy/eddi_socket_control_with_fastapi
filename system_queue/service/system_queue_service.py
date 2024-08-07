from abc import ABC, abstractmethod


class SystemQueueService(ABC):
    @abstractmethod
    def createEssentialSystemQueue(self):
        pass
