import socket

server = socket.socket()
server.bind(("127.0.0.1",8000))
server.listen()

conn,addr = server.accept()
conn.send("Enter number 1: ".encode())
x = conn.recv(128).decode()
conn.send("Enter number 2: ".encode())
y = conn.recv(128).decode()
conn.send(f"Result is: {int(x)+int(y)}".encode())