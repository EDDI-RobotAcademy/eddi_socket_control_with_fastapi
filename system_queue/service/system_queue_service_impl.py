from system_queue.repository.system_queue_repository_impl import SystemQueueRepositoryImpl
from system_queue.service.system_queue_service import SystemQueueService


class SystemQueueServiceImpl(SystemQueueService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__systemQueueRepository = SystemQueueRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def createEssentialSystemQueue(self):
        self.__systemQueueRepository.createEssential()
    