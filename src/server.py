import asyncio
import grpc.aio
import messages_pb2
import messages_pb2_grpc
import time

class GreetingService(messages_pb2_grpc.GreetingServiceServicer):

    async def SayHello(self, request, context):
        time.sleep(1)
        return messages_pb2.HelloReply(message='Hello, {}!'.format(request.name))

async def serve():
    server = grpc.aio.server()
    messages_pb2_grpc.add_GreetingServiceServicer_to_server(GreetingService(), server)
    server.add_insecure_port('[::]:50051')
    await server.start()
    await server.wait_for_termination()

if __name__ == '__main__':
    asyncio.run(serve())