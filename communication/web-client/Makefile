ROOT_DIR:=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
THIRD_PARTY_PATH = ../../third_party
GRPC_WEB_PATH = $(THIRD_PARTY_PATH)/grpc-web
GRPC_WEB_PLUGIN_PATH = $(GRPC_WEB_PATH)/javascript/net/grpc/web/protoc-gen-grpc-web
GRPC_PATH = $(GRPC_WEB_PATH)/third_party/grpc
PROTOBUF_PATH = $(GRPC_PATH)/third_party/protobuf
NGINX_PATH = $(GRPC_WEB_PATH)/third_party/nginx

CLOSURE_LIBRARY_PATH = $(GRPC_WEB_PATH)/third_party/closure-library
PROTOC = protoc
PROTO_DIR = ../
JS_IMPORT_STYLE = import_style=closure,binary
OUT_DIR = ./out
BIN_DIR = ./bin

init:
	cd $(GRPC_WEB_PATH) && git submodule update --init
	$(GRPC_WEB_PATH)/scripts/init_submodules.sh
	sudo apt-get install protobuf-compiler -y
	sudo apt-get install libprotoc-dev -y
	sudo apt-get install unzip -y
	sudo apt-get install default-jdk -y
	cd $(GRPC_WEB_PATH)/javascript/net/grpc/web && make
	wget https://dl.google.com/closure-compiler/compiler-latest.zip -O compiler-latest.zip
	mkdir -p $(BIN_DIR)
	unzip -p -qq -o compiler-latest.zip *.jar > $(BIN_DIR)/closure-compiler.jar
	rm compiler-latest.zip

	# For nginx
	sudo apt-get install autoconf libtool -y
	cd $(PROTOBUF_PATH) && ./autogen.sh && ./configure && make && sudo make install
	cd $(GRPC_PATH) && make CXXFLAGS="-Wno-error=class-memaccess -Wno-error=ignored-qualifiers -Wno-error=stringop-truncation" CFLAGS="-Wno-error=class-memaccess -Wno-error=ignored-qualifiers -Wno-error=stringop-truncation" HAS_SYSTEM_PROTOBUF=false
	pushd $(GRPC_WEB_PATH) && make plugin && sudo make install-plugin && popd
	# Compile Nginx
	sudo apt-get install libpcre3 libpcre3-dev -y
	pushd $(GRPC_WEB_PATH) && make nginx && popd
	pushd $(NGINX_PATH)/src && sudo make install && popd

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

run-proxy:
	/usr/local/nginx/sbin/nginx -p /tmp -c $(ROOT_DIR)/nginx.conf

run:
	sudo python main.py
	