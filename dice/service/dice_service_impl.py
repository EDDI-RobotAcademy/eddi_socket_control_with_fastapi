from dice.repository.dice_repository_impl import DiceRepositoryImpl
from dice.service.dice_service import DiceService
from system_queue.repository.system_queue_repository_impl import SystemQueueRepositoryImpl


class DiceServiceImpl(DiceService):
    def __init__(self, systemQueueRepository: SystemQueueRepositoryImpl):
        self.__diceRepository = DiceRepositoryImpl()
        self.__systemQueueRepository = systemQueueRepository

    def requestListResult(self):
        systemReceiverFastAPIChannel = self.__systemQueueRepository.getSystemSocketReceiverFastAPIChannel()
        return self.__diceRepository.listResult(systemReceiverFastAPIChannel)


