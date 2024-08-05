import os.path
import sys

import colorama
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'include', 'socket_server'))

load_dotenv()

from include.socket_server.acceptor.service.socket_accept_service_impl import SocketAcceptServiceImpl
from include.socket_server.receiver.service.receiver_service_impl import ReceiverServiceImpl
from include.socket_server.server_socket.service.server_socket_service_impl import ServerSocketServiceImpl
from include.socket_server.transmitter.service.transmitter_service_impl import TransmitterServiceImpl
from include.socket_server.task_worker.service.task_worker_service_impl import TaskWorkerServiceImpl
from include.socket_server.utility.color_print import ColorPrinter

from include.socket_server.initializer.init_domain import DomainInitializer

DomainInitializer.initEachDomain()

app = FastAPI()

if __name__ == "__main__":
    colorama.init(autoreset=True)

    serverSocketService = ServerSocketServiceImpl.getInstance()
    serverSocket = serverSocketService.createServerSocket()
    serverSocketService.prepareServerSocket()
    ColorPrinter.print_important_message("Success to create Server Socket")

    socketAcceptService = SocketAcceptServiceImpl.getInstance()
    socketAcceptService.requestToInjectServerSocket(serverSocket)
    ColorPrinter.print_important_message("Success to inject server socket to acceptor")

    taskWorkerService = TaskWorkerServiceImpl.getInstance()
    taskWorkerService.createTaskWorker("Acceptor", socketAcceptService.requestToAcceptClient)
    taskWorkerService.executeTaskWorker("Acceptor")

    receiverService = ReceiverServiceImpl.getInstance()
    receiverService.requestToInjectClientSocket()

    taskWorkerService.createTaskWorker("Receiver", receiverService.requestToReceiveClient)
    taskWorkerService.executeTaskWorker("Receiver")

    transmitterService = TransmitterServiceImpl.getInstance()
    transmitterService.requestToInjectClientSocket()

    taskWorkerService.createTaskWorker("Transmitter", transmitterService.requestToTransmitClient)
    taskWorkerService.executeTaskWorker("Transmitter")

    uvicorn.run(app, host=os.getenv('HOST'), port=int(os.getenv('FASTAPI_PORT')))
