import socket

HOST = "localhost"
PORT = 9000
BUFSIZE = 4096

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST, PORT))

clients = []
while True:
    req, client = server.recvfrom(BUFSIZE)
    if not (client in clients):
        clients.append(client)

    msg = req.decode("UTF-8")
    if msg == "q":
        clients.remove(client)
        continue

    msg = f"{client} > {msg}"
    for client in clients:
        server.sendto(msg.encode("UTF-8"), client)
