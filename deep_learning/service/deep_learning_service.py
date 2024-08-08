from abc import ABC, abstractmethod


class DeepLearningService(ABC):
    @abstractmethod
    def requestAICommand(self, aiCommandRequest):
        pass
