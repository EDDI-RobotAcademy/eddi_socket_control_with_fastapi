import json
import queue

from dice.repository.dice_repository import DiceRepository


class DiceRepositoryImpl(DiceRepository):
    def listResult(self, systemReceiverFastAPIChannel):
        print(f"DiceRepositoryImpl listResult()")

        try:
            receivedResponseFromSocketClient = systemReceiverFastAPIChannel.get(False)
            return json.loads(receivedResponseFromSocketClient)

        except queue.Empty:
            return "아직 데이터를 처리 중이거나 요청한 데이터가 없습니다"
