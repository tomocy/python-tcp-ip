import socket
import datetime

HOST = "localhost"
PORT = 9000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(0)

while True:
    client, addr = server.accept()
    msg = str(datetime.datetime.now())
    client.sendall(msg.encode("UTF-8"))
    print(f"requested from {client}")
    client.close()
