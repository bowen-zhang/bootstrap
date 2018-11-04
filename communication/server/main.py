# Copyright 2018 Bowen Zhang
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import calculator_pb2
import calculator_pb2_grpc
import grpc
import time

from concurrent import futures


class Calculator(calculator_pb2_grpc.CalculatorServicer):
  def Sum(self, request, context):
    print 'Processing request from {0}...'.format(request.client_name)
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