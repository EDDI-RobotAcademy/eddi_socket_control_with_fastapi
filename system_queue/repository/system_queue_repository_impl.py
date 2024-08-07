import multiprocessing

from system_queue.repository.system_queue_repository import SystemQueueRepository


class SystemQueueRepositoryImpl(SystemQueueRepository):
    __instance = None

    __systemSocketReceiverFastAPIChannel = None
    __systemFastAPISocketTransmitterChannel = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def getSystemSocketReceiverFastAPIChannel(self):
        return self.__systemSocketReceiverFastAPIChannel

    def getSystemFastAPISocketTransmitterChannel(self):
        return self.__systemFastAPISocketTransmitterChannel

    def createEssential(self):
        self.__systemSocketReceiverFastAPIChannel = multiprocessing.Queue()
        self.__systemFastAPISocketTransmitterChannel = multiprocessing.Queue()
    