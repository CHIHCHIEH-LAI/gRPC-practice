from concurrent import futures
import grpc
import messages_pb2
import messages_pb2_grpc

class GreetingService(messages_pb2_grpc.GreetingServiceServicer):

    def SayHello(self, request, context):
        return messages_pb2.HelloReply(message='Hello, {}!'.format(request.name))

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    messages_pb2_grpc.add_GreetingServiceServicer_to_server(GreetingService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
