# What

Serializes and deserializes data across platform/language.

# How

1. Install Protobuf Compiler

    * Mac

        ```shell
        brew install protobuf
        ```

        Alternatively:

        ```shell
        curl -L -o protoc.zip https://github.com/protocolbuffers/protobuf/releases/download/v3.6.1/protoc-3.6.1-osx-x86_64.zip
        sudo unzip -o protoc.zip -d /usr/local bin/protoc
        rm -f protoc.zip
        ```

    * Linux

        ```shell
        curl -L -o protoc.zip https://github.com/protocolbuffers/protobuf/releases/download/v3.6.1/protoc-3.6.1-linux-x86_64.zip
        sudo unzip -o protoc.zip -d /usr/local bin/protoc
        rm -f protoc.zip
        ```

1. Define Protobuf

    Example: data.proto
    ```
    message MyData {
        string name = 1;
        int32 value = 2;
    }
    ```

    See [Protobuf language guide](https://developers.google.com/protocol-buffers/docs/proto3) for more information.

1. Compile Protobuf

    ```shell
    protoc -I=. --python_out=. ./data.proto
    ```

1. Serialization

    * To JSON format

        ```python
        from google.protobuf import json_format
        import data_pb2
        ...
        proto = data_pb2.MyData()
        ...
        proto_json = json_format.MessageToJson(proto)
        ...
        ```

    * To text format

        ```python
        from google.protobuf import text_format
        import data_pb2
        ...
        proto = data_pb2.MyData()
        ...
        proto_text = text_format.MessageToString(proto)
        ...
        ```

    * To binary format

        ```python
        import data_pb2
        ...
        proto = data_pb2.MyData()
        ...
        binary = proto.SerializeToString()
        ...
        ```

1. Deserialization

    * From text format

        ```python
        from google.protobuf import text_format
        import data_pb2
        ...
        proto = data_pb2.MyData()
        text_format.Merge(proto_text, proto)
        ...
        ```

    * From binary format

        ```python
        import data_pb2
        ...
        proto = data_pb2.MyData()
        proto.ParseFromString(binary)
        ...
        ```

# Resources

* [Protobuf Source Code](https://github.com/protocolbuffers/protobuf)