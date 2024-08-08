import json

from dice.repository.dice_repository import DiceRepository


class DiceRepositoryImpl(DiceRepository):
    def listResult(self, systemReceiverFastAPIChannel):
        print(f"DiceRepositoryImpl listResult()")
        receivedResponseFromSocketClient = systemReceiverFastAPIChannel.get()

        return json.loads(receivedResponseFromSocketClient)
