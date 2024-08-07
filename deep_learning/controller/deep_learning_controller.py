from fastapi import APIRouter, Depends, status
from starlette.responses import JSONResponse

from deep_learning.controller.request_form.ai_command_request_form import AICommandRequestForm
from deep_learning.service.deep_learning_service_impl import DeepLearningServiceImpl

deepLearningRouter = APIRouter()

async def injectDeepLearningService() -> DeepLearningServiceImpl:
    return DeepLearningServiceImpl()

@deepLearningRouter.post("/request-ai-command")
async def requestAiCommand(aiCommandRequestForm: AICommandRequestForm,
                           deepLearningService: DeepLearningServiceImpl =
                           Depends(injectDeepLearningService)):

    deepLearningService.requestAICommand(aiCommandRequestForm.toAICommandRequest())

    return JSONResponse(content=True, status_code=status.HTTP_200_OK)
