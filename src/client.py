import grpc
import messages_pb2
import messages_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = messages_pb2_grpc.GreetingServiceStub(channel)
        response = stub.SayHello(messages_pb2.HelloRequest(name='Alice'))
        print("Greeting client received: " + response.message)

if __name__ == '__main__':
    run()
