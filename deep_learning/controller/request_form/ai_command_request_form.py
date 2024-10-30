from typing import Optional, Union, Any, List
from pydantic import BaseModel

from deep_learning.service.request.ai_command_request import AICommandRequest


class AICommandRequestForm(BaseModel):
    command: int
    data: Optional[Union[Any, List[Any]]] = None

    def toAICommandRequest(self) -> AICommandRequest:
        return AICommandRequest(command=self.command, data=self.data)
