

import socket

co = socket.socket()

co.connect(("localhost", 9999))

name = input("Enter your name :  ")
co.send(bytes(name, 'utf-8'))

print(co.recv(1024).decode())

while True:

        msg = co.recv(1024).decode()
        print(msg)

        msg = input("{} >>>  ".format(name))
        co.send(bytes(msg, 'utf-8'))
