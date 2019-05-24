import socket
import threading
import sys

HOST = "localhost"
PORT = 9000
BUFSIZE = 4096


def receive(client):
    while True:
        try:
            resp = client.recv(BUFSIZE)
        except:
            break

        msg = resp.decode("UTF-8")
        print(msg)

    client.close()


client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

thre = threading.Thread(target=receive, args=(client,))
thre.setDaemon(True)

while True:
    inputed = input()
    msg = inputed.encode("UTF-8")
    client.sendto(msg, (HOST, PORT))
    if inputed == "q":
        break

    if not thre.is_alive():
        thre.start()

client.close()
