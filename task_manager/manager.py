import os
import sys

from dotenv import load_dotenv

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'include', 'socket_server'))

load_dotenv()

from include.socket_server.acceptor.service.socket_accept_service_impl import SocketAcceptServiceImpl
from include.socket_server.receiver.service.receiver_service_impl import ReceiverServiceImpl
from include.socket_server.server_socket.service.server_socket_service_impl import ServerSocketServiceImpl
from include.socket_server.task_worker.service.task_worker_service_impl import TaskWorkerServiceImpl
from include.socket_server.transmitter.service.transmitter_service_impl import TransmitterServiceImpl
from include.socket_server.utility.color_print import ColorPrinter


class TaskManager(object):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    @staticmethod
    def createSocketServer():
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
        receiverService.requestToInjectFastAPIReceiverChannel()

        taskWorkerService.createTaskWorker("Receiver", receiverService.requestToReceiveClient)
        taskWorkerService.executeTaskWorker("Receiver")

        transmitterService = TransmitterServiceImpl.getInstance()
        transmitterService.requestToInjectClientSocket()

        # TODO: transmitter와 fastapi간 IPC Channel 구성 필요함

        taskWorkerService.createTaskWorker("Transmitter", transmitterService.requestToTransmitClient)
        taskWorkerService.executeTaskWorker("Transmitter")