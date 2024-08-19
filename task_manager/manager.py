import os
import sys

from dotenv import load_dotenv

from system_queue.repository.system_queue_repository_impl import SystemQueueRepositoryImpl

try:
    from user_defined_queue.repository.user_defined_queue_repository_impl import UserDefinedQueueRepositoryImpl
except ImportError:
    UserDefinedQueueRepositoryImpl = None

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'include', 'socket_server'))

load_dotenv()

from include.socket_server.acceptor.service.socket_accept_service_impl import SocketAcceptServiceImpl
from include.socket_server.receiver.service.receiver_service_impl import ReceiverServiceImpl
from include.socket_server.server_socket.service.server_socket_service_impl import ServerSocketServiceImpl
from include.socket_server.thread_worker.service.thread_worker_service_impl import ThreadWorkerServiceImpl
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

        threadWorkerService = ThreadWorkerServiceImpl.getInstance()
        threadWorkerService.createThreadWorker("Acceptor", socketAcceptService.requestToAcceptClient)
        threadWorkerService.executeThreadWorker("Acceptor")

        systemQueueRepository = SystemQueueRepositoryImpl.getInstance()
        systemFastAPITransmitterChannel = systemQueueRepository.getSystemFastAPISocketTransmitterChannel()
        systemReceiverFastAPIChannel = systemQueueRepository.getSystemSocketReceiverFastAPIChannel()

        receiverService = ReceiverServiceImpl.getInstance()
        receiverService.requestToInjectReceiverFastAPIChannel(systemReceiverFastAPIChannel)

        if UserDefinedQueueRepositoryImpl is not None:
            userDefinedQueueRepository = UserDefinedQueueRepositoryImpl.getInstance()
            userDefinedReceiverFastAPIChannel = userDefinedQueueRepository.getUserDefinedSocketReceiverFastAPIChannel()

            receiverService.requestToInjectUserDefinedReceiverFastAPIChannel(userDefinedReceiverFastAPIChannel)

        threadWorkerService.createThreadWorker("Receiver", receiverService.requestToReceiveClient)
        threadWorkerService.executeThreadWorker("Receiver")

        transmitterService = TransmitterServiceImpl.getInstance()
        transmitterService.requestToInjectFastAPITransmitterChannel(systemFastAPITransmitterChannel)

        threadWorkerService.createThreadWorker("Transmitter", transmitterService.requestToTransmitClient)
        threadWorkerService.executeThreadWorker("Transmitter")