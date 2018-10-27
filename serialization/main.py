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

from google.protobuf import json_format
from google.protobuf import text_format

import data_pb2


def main():
  product_proto = data_pb2.Product()

  with open('data.protoascii', 'r') as f:
    text_format.Merge(f.read(), product_proto)

  product_json = json_format.MessageToJson(product_proto)
  print product_json

  with open('data.bin', 'wb') as f:
    f.write(product_proto.SerializeToString())


if __name__ == '__main__':
  main()