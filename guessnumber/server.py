import socket
import random

server = socket.socket()
server.bind(("localhost", 8000))
server.listen()

while True:
    conn,addr = server.accept()
    conn.send("Enter number: ".encode())
    my_num = random.randint(1,5)
    client_num = conn.recv(256).decode()
    if my_num == int(client_num):
        conn.send(f"Nice! I guessed that number".encode())
    else:
        conn.send(f"Wrong! I guessed {my_num} and you typed {client_num}...".encode())