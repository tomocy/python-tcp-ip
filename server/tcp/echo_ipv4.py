import socket
import datetime

HOST = "localhost"
PORT = 9000
BUFSIZE = 4096

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(0)

while True:
    client, addr = server.accept()
    print(f"requested from {client}")

    req = client.recv(BUFSIZE)
    print(req.decode("UTF-8"))

    msg = str(datetime.datetime.now())
    client.sendall(msg.encode("UTF-8"))
    client.close()
