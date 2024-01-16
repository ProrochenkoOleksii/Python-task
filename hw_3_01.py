# UDP-комунікація:
# Створіть простий UDP-сервер, який може приймати дані від клієнтів.

# * потрібно буде використати функцію recvfrom() замість recv() як це було
# для TCP протоколу реалізовано

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


# Напишіть клієнтський додаток, який відправляє дані на сервер та очікує відповіді.

HOST = "127.0.0.1"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.sendto(b"Hello world", (HOST, PORT))
    data, addr = s.recvfrom(1024)

print("Received from {}: {}".format(addr, repr(data)))

