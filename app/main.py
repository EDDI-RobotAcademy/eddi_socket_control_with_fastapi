import os.path
import sys

import colorama

import uvicorn
from fastapi import FastAPI

from task_manager.manager import TaskManager
from include.socket_server.initializer.init_domain import DomainInitializer

DomainInitializer.initEachDomain()

app = FastAPI()

if __name__ == "__main__":
    colorama.init(autoreset=True)

    TaskManager.createSocketServer()
    uvicorn.run(app, host=os.getenv('HOST'), port=int(os.getenv('FASTAPI_PORT')))
