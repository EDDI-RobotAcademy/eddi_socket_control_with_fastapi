class SystemInitializer:
    @staticmethod
    def initIPCQueueDomain():
        ipcQueueService = IPCQueueServiceImpl.getInstance()
        ipcQueueService.createDefaultIPCQueue()

    @staticmethod
    def initSystemDomain():

        SystemInitializer.initIPCQueueDomain()