import socket
import threading

HOST = "localhost"
PORT = 9000
BUFSIZE = 4096


def receive_and_send_all(client, addr):
    while True:
        try:
            req = client.recv(BUFSIZE)
        except:
            clients.remove(client)
            break

        if not req:
            clients.remove(client)
            break
        decoded = req.decode("UTF-8")
        if decoded == "q":
            clients.remove(client)
            break

        msg = f"{addr} > {decoded}"
        encoded = msg.encode("UTF-8")
        for client in clients:
            client.sendall(encoded)

    client.close()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(0)

clients = []
while True:
    client, addr = server.accept()
    clients.append(client)
    thre = threading.Thread(target=receive_and_send_all, args=(client, addr))
    thre.start()
