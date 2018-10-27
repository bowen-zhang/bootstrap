import calculator_pb2
import calculator_pb2_grpc
import grpc


def main():
  channel = grpc.insecure_channel('localhost:50051')
  stub = calculator_pb2_grpc.CalculatorStub(channel)
  request = calculator_pb2.Request(
      client_name='Test Client', values=[1, 2, 3, 4, 5])
  response = stub.Sum(request)

  print response.message


if __name__ == '__main__':
  main()