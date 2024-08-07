from abc import ABC, abstractmethod

from deep_learning.repository.deep_learning_repository_impl import DeepLearningRepositoryImpl
from deep_learning.service.deep_learning_service import DeepLearningService


class DeepLearningServiceImpl(DeepLearningService):
    def __init__(self):
        self.__deepLearningRepository = DeepLearningRepositoryImpl()

    def requestAICommand(self, aiCommandRequest):
        self.__deepLearningRepository.requestToSocketServer(aiCommandRequest)
    