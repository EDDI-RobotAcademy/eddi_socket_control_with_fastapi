from abc import ABC, abstractmethod


class DiceRepository(ABC):
    @abstractmethod
    def listResult(self, systemReceiverFastAPIChannel):
        pass
