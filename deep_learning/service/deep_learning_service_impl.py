from deep_learning.repository.deep_learning_repository_impl import DeepLearningRepositoryImpl
from deep_learning.service.deep_learning_service import DeepLearningService
from system_queue.repository.system_queue_repository_impl import SystemQueueRepositoryImpl


class DeepLearningServiceImpl(DeepLearningService):
    def __init__(self, systemQueueRepository: SystemQueueRepositoryImpl):
        self.__deepLearningRepository = DeepLearningRepositoryImpl()
        self.__systemQueueRepository = systemQueueRepository

    def requestAICommand(self, aiCommandRequest):
        systemFastAPITransmitterChannel = self.__systemQueueRepository.getSystemFastAPISocketTransmitterChannel()
        self.__deepLearningRepository.requestToSocketServer(aiCommandRequest, systemFastAPITransmitterChannel)
    