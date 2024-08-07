import multiprocessing

from ipc_queue.repository.ipc_queue_repository import IPCQueueRepository


class IPCQueueRepositoryImpl(IPCQueueRepository):
    __instance = None

    __ipcFastAPISocketReceiverChannel = None
    __ipcSocketTransmitterFastAPIChannel = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def getIPCFastAPISocketReceiverChannel(self):
        return self.__ipcFastAPISocketReceiverChannel

    def getIPCSocketTransmitterFastAPIChannel(self):
        return self.__ipcSocketTransmitterFastAPIChannel

    def createEssential(self):
        self.__ipcFastAPISocketReceiverChannel = multiprocessing.Queue()
        self.__ipcSocketTransmitterFastAPIChannel = multiprocessing.Queue()
    