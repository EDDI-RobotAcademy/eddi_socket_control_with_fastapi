from fastapi import APIRouter, Depends, status
from starlette.responses import JSONResponse

from dice.service.dice_service_impl import DiceServiceImpl
from include.socket_server.utility.color_print import ColorPrinter
from system_queue.repository.system_queue_repository_impl import SystemQueueRepositoryImpl

diceResultRouter = APIRouter()

async def injectDiceService() -> DiceServiceImpl:
    return DiceServiceImpl(
        SystemQueueRepositoryImpl.getInstance())

@diceResultRouter.post("/dice-result")
async def requestDiceResult(diceService: DiceServiceImpl =
                            Depends(injectDiceService)):

    diceListResult = diceService.requestListResult()
    ColorPrinter.print_important_data("requestDiceResult", diceListResult)

    return JSONResponse(content=diceListResult, status_code=status.HTTP_200_OK)
