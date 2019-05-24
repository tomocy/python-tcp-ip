import socket
import sys

HOST = "localhost"
PORT = 9000
DATAFILE = "./data.txt"

file = open(DATAFILE, "rt")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client.connect((HOST, PORT))
except:
    print("failed to connect")
    sys.exit()

msg = file.read()
client.sendall(msg.encode("UTF-8"))

client.close()
