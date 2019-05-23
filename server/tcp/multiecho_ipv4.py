import socket
import datetime
import threading

HOST = "localhost"
PORT = 9000
BUFSIZE = 4096


def echo(client, clino, msg):
    req = client.recv(BUFSIZE)
    print(f"{req.decode('UTF-8')} (client number: {clino})")
    client.sendall(msg.encode("UTF-8"))
    client.close()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(0)

clino = 0
while True:
    client, addr = server.accept()
    clino += 1
    print(f"requested from {client} (clinet number: {clino})")
    msg = str(datetime.datetime.now())
    thre = threading.Thread(target=echo, args=(client, clino, msg))
    thre.start()
