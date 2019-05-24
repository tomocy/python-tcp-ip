import socket
import datetime

HOST = "localhost"
PORT = 9000
BUFSIZE = 4096

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(0)

while True:
    client, adrr = server.accept()
    print(f"requested from {client}")
    timestr = datetime.datetime.now().strftime("%m%d%H%M%S%f")
    dname = "../../../resource"
    fname = f"{dname}/{timestr}.txt"
    file = open(fname, "wt")
    while True:
        req = client.recv(BUFSIZE)
        if not req:
            break

        try:
            print(req.decode("UTF-8"), file=file)
        except:
            print("something went wrong")
            break

    client.close()
    file.close()
