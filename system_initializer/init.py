from system_queue.service.system_queue_service_impl import SystemQueueServiceImpl


class SystemInitializer:
    @staticmethod
    def initSystemQueueDomain():
        systemQueueService = SystemQueueServiceImpl.getInstance()
        systemQueueService.createEssentialSystemQueue()

    @staticmethod
    def initSystemDomain():
        SystemInitializer.initSystemQueueDomain()
