import socket

client = socket.socket()
client.connect(("127.0.0.1",8000))

x = input(client.recv(256).decode())
client.send(x.encode())
y = input(client.recv(256).decode())
client.send(y.encode())

print(client.recv(256).decode())