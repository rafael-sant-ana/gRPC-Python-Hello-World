import hello_pb2

msg = hello_pb2.HelloMessage(
    name="Raf",
    greeting="Hello"
)

# to binary
binary = msg.SerializeToString()
print(f"serialized: {len(binary)} bytes")

# back to msg
parsed = hello_pb2.HelloMessage()
parsed.ParseFromString(binary)

print(f"Deserialized: {parsed.greeting}, {parsed.name}!")