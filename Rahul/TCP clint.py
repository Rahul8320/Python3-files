# For TCP clint

import socket

target_host = "localhost"
target_port = 9999

# create a socket object with IPv4 address and TCP clint
clint = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the clint
clint.connect((target_host, target_port))
print("We r connected ")
# send some data
clint.send(bytes("WELCOME TO SERVER ", 'utf-8'))
print("Send successful")
# receive some data
response = clint.recv(4096).decode()
print("Receive successful")
print(response)
