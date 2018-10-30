ROOT_DIR:=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

init:
	pip install -r requirements.txt --user

proto:
	python -m grpc_tools.protoc -I=. --python_out=. --grpc_python_out=. ./calculator.proto

run-server:
	PYTHONPATH=$(ROOT_DIR) python server/main.py

run-client:
	PYTHONPATH=$(ROOT_DIR) python client/main.py

run-web-client:
	cd web-client && make run
