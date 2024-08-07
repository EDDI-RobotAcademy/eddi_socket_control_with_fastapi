from abc import ABC, abstractmethod


class IPCQueueRepository(ABC):
    @abstractmethod
    def createEssential(self):
        pass
