from abc import ABC, abstractmethod


class DeepLearningRepository(ABC):
    @abstractmethod
    def requestToSocketServer(self, request, systemFastAPITransmitterChannel):
        pass
