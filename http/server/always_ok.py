import socket

HOST = "localhost"
PORT = 9000
BUFSIZE = 4096
RESP_FILENAME = "./index.html"

file = open(RESP_FILENAME, "rt")
respBody = file.read()
file.close()
respBody = f"HTTP/1.0 200 OK\n\n{respBody}"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(0)

while True:
    client, addr = server.accept()
    msg = client.recv(BUFSIZE)
    decoded = msg.decode("UTF-8")
    print(decoded)

    encoded = respBody.encode("UTF-8")
    client.sendall(encoded)
    client.close()
