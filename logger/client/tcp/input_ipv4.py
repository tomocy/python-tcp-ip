import socket
import sys

HOST = "localhost"
PORT = 9000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client.connect((HOST, PORT))
except:
    print("failed to connect")
    sys.exit()

while True:
    msg = input()
    if msg == "q":
        break

    client.sendall(msg.encode("UTF-8"))

client.close()
