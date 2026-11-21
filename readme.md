
Needs to be installed:
in python, protobuf: pip install protobuf
in linux, apt install protobuf-compiler

To compile .proto file:

protoc --python_out=. hello.proto

