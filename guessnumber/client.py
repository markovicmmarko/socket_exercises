import socket

client = socket.socket()
client.connect(("127.0.0.1",8000))

num = input(client.recv(256).decode())
client.send(num.encode())
print(client.recv(512).decode())