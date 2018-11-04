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


def main():
  channel = grpc.insecure_channel('localhost:50051')
  stub = calculator_pb2_grpc.CalculatorStub(channel)
  request = calculator_pb2.Request(
      client_name='Test Client', values=[1, 2, 3, 4, 5])
  response = stub.Sum(request)

  print response.message


if __name__ == '__main__':
  main()