# UDP communication:
# Create a simple UDP server that can accept data from clients.

# * will need to use the recvfrom() function instead of recv() as it was
# for the TCP protocol is implemented

import socket

HOST = "127.0.0.1"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind ((HOST, PORT))
    print("Connected by {}:{}".format(HOST, PORT))
    while True:
        data, addr = s.recvfrom(1024)
        if not data:
            break
        print("Received data from {}: {}".format(addr, data.decode()))
        s.sendto(data.upper(), addr)


# Write a client application that sends data to the server and waits for a response.

HOST = "127.0.0.1"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.sendto(b"Hello world", (HOST, PORT))
    data, addr = s.recvfrom(1024)

print("Received from {}: {}".format(addr, repr(data)))

