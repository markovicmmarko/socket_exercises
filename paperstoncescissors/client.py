import socket

client = socket.socket()
client.connect(("127.0.0.1",8000))

print("Choose object:\n")
print(client.recv(128).decode())
client.send(input("").encode())

print(client.recv(256).decode())
print(client.recv(256).decode())
print(client.recv(256).decode())
