import os.path
from fastapi.middleware.cors import CORSMiddleware

import colorama

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI

from deep_learning.controller.deep_learning_controller import deepLearningRouter
from dice.controller.dice_controller import diceResultRouter
from system_initializer.init import SystemInitializer
from task_manager.manager import TaskManager
from include.socket_server.initializer.init_domain import DomainInitializer

DomainInitializer.initEachDomain()
SystemInitializer.initSystemDomain()

app = FastAPI()

load_dotenv()

origins = os.getenv("ALLOWED_ORIGINS", "").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(deepLearningRouter)
app.include_router(diceResultRouter)

if __name__ == "__main__":
    colorama.init(autoreset=True)

    TaskManager.createSocketServer()
    uvicorn.run(app, host=os.getenv('HOST'), port=int(os.getenv('FASTAPI_PORT')))
