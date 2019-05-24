import socket
import sys
import os
import time

HOST = "localhost"
PORT = 9000
SLEEPSEC = 10

while True:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((HOST, PORT))
    except:
        print("failed to connect")
        sys.exit()

    msg = str(os.getloadavg())
    client.sendall(msg.encode("UTF-8"))

    client.close()
    time.sleep(SLEEPSEC)
