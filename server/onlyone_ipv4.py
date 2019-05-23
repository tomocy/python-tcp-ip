import socket

HOST = "localhost"
PORT = 9000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(0)

client, addr = server.accept()
client.sendall(b"Hello, world\n")

client.close()
server.close()
