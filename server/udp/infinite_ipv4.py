import socket
import datetime

HOST = "localhost"
PORT = 9000
BUFSIZE = 4096

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST, PORT))

while True:
    req, client = server.recvfrom(BUFSIZE)
    msg = str(datetime.datetime.now())
    server.sendto(msg.encode("UTF-8"), client)
    print(f"requested from {client}")
