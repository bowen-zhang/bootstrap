import calculator_pb2
import calculator_pb2_grpc
import grpc
import time

from concurrent import futures


class Calculator(calculator_pb2_grpc.CalculatorServicer):
  def Sum(self, request, context):
    response = calculator_pb2.Response()
    response.message = '{0} has sum value of {1}.'.format(
        request.client_name, sum(request.values))
    return response


def main():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  calculator_pb2_grpc.add_CalculatorServicer_to_server(Calculator(), server)
  server.add_insecure_port('[::]:50051')
  server.start()
  while True:
    time.sleep(1)


if __name__ == '__main__':
  main()