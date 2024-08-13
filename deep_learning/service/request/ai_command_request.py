from typing import Optional, Union, Any, List
from pydantic import BaseModel


class AICommandRequest(BaseModel):
    command: int
    data: Optional[Union[Any, List[Any]]] = None

    def getCommand(self):
        return self.command

    def getDataList(self):
        return self.data
