import grpc.aio
import asyncio
import messages_pb2
import messages_pb2_grpc

async def run():
    async with grpc.aio.insecure_channel('localhost:50051') as channel:
        stub = messages_pb2_grpc.GreetingServiceStub(channel)
        for i in range(100):
            response = await stub.SayHello(messages_pb2.HelloRequest(name='Alice'+str(i)))
            print("Greeting client received: " + response.message)

if __name__ == '__main__':
    asyncio.run(run())
