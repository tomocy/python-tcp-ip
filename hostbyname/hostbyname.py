import socket

while True:
    try:
        name = input("Enter host name (q to quit)")
        if name == "q":
            break

        print(socket.gethostbyname(name))
    except:
        print("failed to get host by name")
