PROTOC = protoc
PROTO_DIR = ../
PROTOBUF_PATH = ./third_party/protobuf
CLOSURE_LIBRARY_PATH = ./third_party/closure-library
GRPC_WEB_PATH = ./third_party/grpc-web
GRPC_WEB_PLUGIN_PATH = $(GRPC_WEB_PATH)/javascript/net/grpc/web/protoc-gen-grpc-web
JS_IMPORT_STYLE = import_style=closure,binary
OUT_DIR = ./out
BIN_DIR = ./bin

init:
	#git submodule update --init
	#sudo apt-get install protobuf-compiler
	#sudo apt-get install libprotoc-dev
	cd third_party/grpc-web/javascript/net/grpc/web && make
	wget https://dl.google.com/closure-compiler/compiler-latest.zip -O compiler-latest.zip
	mkdir -p $(BIN_DIR)
	unzip -p -qq -o compiler-latest.zip *.jar > $(BIN_DIR)/closure-compiler.jar
	rm compiler-latest.zip


run: proto-py proto-js compiled-js
	python core.py

proto-py:
	$(PROTOC) -I=$(PROTO_DIR) --python_out=$(PROTO_DIR) $(PROTO_DIR)/*.proto

proto-js:
	rm -rf $(OUT_DIR)
	mkdir -p $(OUT_DIR)
	$(PROTOC) -I=$(PROTO_DIR) --js_out=library=calculator,binary:$(OUT_DIR) $(PROTO_DIR)/*.proto
	$(PROTOC) -I=$(PROTO_DIR) \
			  --plugin=protoc-gen-grpc-web=$(GRPC_WEB_PLUGIN_PATH) \
			  --grpc-web_out=import_style=closure,mode=grpcwebtext:$(OUT_DIR) \
			  $(PROTO_DIR)/calculator.proto

compiled-js: proto-js
	java \
		-jar $(BIN_DIR)/closure-compiler.jar \
		--js $(GRPC_WEB_PATH)/javascript \
  		--js $(GRPC_WEB_PATH)/net \
  		--js $(CLOSURE_LIBRARY_PATH) \
  		--js $(PROTOBUF_PATH)/js \
  		--js $(OUT_DIR) \
  		--entry_point=goog:proto.CalculatorClient \
  		--dependency_mode=STRICT \
  		--js_output_file static/calculator.js
	