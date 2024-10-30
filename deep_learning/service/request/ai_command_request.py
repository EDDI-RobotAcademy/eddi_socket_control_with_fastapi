from typing import Optional, Union, Any, List
from pydantic import BaseModel


class AICommandRequest(BaseModel):
    userToken: str
    command: int
    data: Optional[Union[Any, List[Any]]] = None

    def getUserToken(self):
        return self.userToken

    def getCommand(self):
        return self.command

    def getDataList(self):
        return self.data
