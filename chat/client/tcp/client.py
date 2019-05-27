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
        if not resp:
            break

        decoded = resp.decode("UTF-8")
        print(decoded)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client.connect((HOST, PORT))
except:
    print("failed to connect")
    sys.exit()

thre = threading.Thread(target=receive, args=(client,))
thre.start()

while True:
    msg = input()
    encoded = msg.encode("UTF-8")
    client.sendall(encoded)
    if msg == "q":
        break

client.close()
