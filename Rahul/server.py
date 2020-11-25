
import socket

s = socket.socket()
so = socket.socket()

print(" Socket created ...")

s.bind(("localhost", 9999))
so.bind(("localhost", 9990))

s.listen(3)
so.listen(3)

print("Waiting for connection ....")

while True:

    c, add = s.accept()
    name1 = c.recv(10240).decode()
    print("Connected with ", add, name1)
    c.send(bytes("You r connected ... ", 'utf-8'))

    co, addr = so.accept()
    name2 = co.recv(1024).decode()
    print("Connected with  ", addr, name2)
    co.send(bytes("you r connected...", 'utf-8'))

    while True:

        msg = c.recv(1024).decode()
        co.send(bytes(name1 + "  >>>  " + msg, 'utf-8'))

        msg = co.recv(1024).decode()
        c.send(bytes(name2 + "  >>>  " + msg, 'utf-8'))

    c.close()
    co.close()

