import socket

HOST = "localhost"
PORT = 9000

BUFSIZE = 4096

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

resp = client.recv(BUFSIZE)
print(resp.decode("UTF-8"))

client.close()
