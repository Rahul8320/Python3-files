
import socket
import threading

bind_ip = "localhost"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip, bind_port))

server.listen(5)
print("[*] Listing on %s:%d" % (bind_ip, bind_port))

# this is our clint-handling thread


def handle_client(client_socket):

    # print out what the clint send
    request = client_socket.recv(1024).decode()

    print(" [*] Received : %s " % request)
    # send back a packet
    client_socket.send(bytes("ACK!", 'utf-8'))

    client_socket.close()


while True:

    client, addr = server.accept()

    print(" [*] Accepted connection from : %s:%d" % (addr[0], addr[1]))

    # spin up our clint thread to handle incoming data
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()

 