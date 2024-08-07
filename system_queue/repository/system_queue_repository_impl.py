import multiprocessing

from system_queue.repository.system_queue_repository import SystemQueueRepository


class SystemQueueRepositoryImpl(SystemQueueRepository):
    __instance = None

    __systemFastAPISocketReceiverChannel = None
    __systemSocketTransmitterFastAPIChannel = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def getSystemFastAPISocketReceiverChannel(self):
        return self.__systemFastAPISocketReceiverChannel

    def getSystemSocketTransmitterFastAPIChannel(self):
        return self.__systemSocketTransmitterFastAPIChannel

    def createEssential(self):
        self.__systemFastAPISocketReceiverChannel = multiprocessing.Queue()
        self.__systemSocketTransmitterFastAPIChannel = multiprocessing.Queue()
    