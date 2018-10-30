# What

Communicate / make procedure calls from client to server across network.

# How

## Protobuf

1. Define a proto to serve as contract between client and server.

    demo.proto

    ```proto
    syntax = "proto3";

    message Request {
        // some fields
    }

    message Response {
        // some fields
    }

    service MyService {
        rpc Test(Request) returns (Response);
    }
    ```

1. Build proto

    ```shell
    pip install grpcio-tools
    python -m grpc_tools.protoc -I=. --python_out=. --grpc_python_out=. ./demo.proto
    ```
    
## Backend Client

1. Imports generated proto python modules.

    Python module for protobuf messages is named as [proto filename]_pb2.py.

    Python module for gRPC services is named as [proto filename]_pb2_grpc.py.

    ```python
    import demo_pb2
    import demo_pb2_grpc
    import grpc
    ```

1. Creates a channel.

    ```python
    channel = grpc.insecure_channel('localhost:50051')
    ```

1. Creates service stub.

    ```python
    stub = demo_pb2_grpc.MyServiceStub(channel)
    ```

1. Call service method.

    ```python
    request = demo_pb2.Request()
    # sets field values...
    response = stub.Test(request)
    ```

## Backend Server

1. Imports generated proto python modules.

    ```python
    import demo_pb2
    import demo_pb2_grpc
    import grpc
    import time

    from concurrent import futures
    ```

1. Implements service class.

    ```python
    class MyService(demo_pb2_grpc.MyServiceServicer):
    def Test(self, request, context):
      # process the request.
      response = demo_pb2.Response()
      # sets response fields.
      return response
    ```

1. Creates server.

    ```python
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ```

1. Register services.

    ```python
    demo_pb2_grpc.add_MyServiceServicer_to_server(MyService(), server)
    ```

1. Starts server.

    ```python
    server.add_insecure_port('[::]:50051')
    server.start()
    while True:
      time.sleep(1)
    ```

## Web Client

To use grpc from web client, it takes significant effort for a one-time setup.
Afterwards, it is extremely convenient to make remote procedure calls from
Javascript using exactly tne same data structure as used in backend service.

The most value comes when streaming is needed. There's no additional changes
required at server side, and it is very transparent at web client side.

1. Add grpc-web submodule

    ```shell
    make third_party
    cd third_party
    git submodule add https://github.com/grpc/grpc-web
    ```

1. Build grpc-web

    See web-client/Makefile:init.

    Note:
    * The entire build process may take 1+ hour.

    * If Google Cloud Compute Engine is used, make sure to use machine type
    "g1-small". Memory of "f1-micro" is too small to build protobuf and will
    hang the VM.

1. Starts Nginx.

    1. Creates Nginx configuration file.

        See web-client/nginx.conf

    1. Run Nginx.

        ```shell
        /usr/local/nginx/sbin/nginx -p /tmp -c [absolute path to nginx.conf]
        ```

1. Open port on VM

    1. Logins on console.cloud.google.com.
    1. Goes to VPC networks, Firewall rules.
    1. Creates firewall rule.
        * Name: "grpc-web"
        * Targets: "specified target tags"
        * Target tags: "grpc-web"
        * Source filter: "IP ranges"
        * Source IP ranges: "0.0.0.0/0"
        * Protocols and ports: "Specified protocols and ports"
        * tcp: "50052"
    1. Goes to Compute Engine, VM instances
    1. Edit the instance
        * Network tags: add "grpc-web"

1. Create web client.

    1. Includes generated js file in html.

        ```html
        <script src="demo.js"></script>
        ```

    1. Creates service stub.

        ```javascript
        var service = new proto.MyServiceClient('http://' + window.location.hostname + ':50052');
        ```

    1. Calls service method.

        ```javascript
        var request = new proto.Request();
        // sets request fields.
        service.test(request, {}, function(err, response) {
            // gets response fields.
        });
        ```

# Resources

* [Protobuf](https://developers.google.com/protocol-buffers/)
* [gRPC](https://grpc.io/)
* [gRPC Web GitHub](https://github.com/grpc/grpc-web)