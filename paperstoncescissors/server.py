import socket
import random

server = socket.socket()
server.bind(("localhost",8000))
server.listen()

conn,addr = server.accept()
objects = {
    "1": "Paper",
    "2": "Stone",
    "3": "Scissors"
}

for k,v in objects.items():
    conn.send(f"{k} = {v}\n".encode())

conn_select = int(conn.recv(128))
comp_select = random.randint(1,3)

print(f"Your selection: {conn_select}\n")
conn.send(f"You selected {objects[str(conn_select)]}\n".encode())
conn.send(f"I selected {objects[str(comp_select)]}\n".encode())

if (conn_select == 1 and comp_select == 2) or (conn_select == 2 and comp_select == 3) or (conn_select == 3 and comp_select == 1):
    conn.send("You won!".encode())
elif conn_select == comp_select:
    conn.send("Even".encode())
else:
    conn.send("I won...".encode())
