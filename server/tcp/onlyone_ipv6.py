import socket

HOST = "localhost"
PORT = 9000

server = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(0)

client, arr = server.accept()
client.sendall(b"Hello, world in ipv6")

client.close()
server.close()
