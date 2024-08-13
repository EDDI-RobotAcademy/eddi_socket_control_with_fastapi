from deep_learning.repository.deep_learning_repository import DeepLearningRepository


class DeepLearningRepositoryImpl(DeepLearningRepository):
    def requestToSocketServer(self, request, systemFastAPITransmitterChannel):
        print(f"DeepLearningRepositoryImpl requestToSocketServer() -> request: {request}")
        systemFastAPITransmitterChannel.put(request.json())
    