
# for UDP clint

import socket

target_host = "100.76.9.149"
target_port = 80

# creat a socket object with IPv4 address and UDP clint
clint = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Socket Created .")

# send some data
clint.sendto(bytes("www.google.com",'utf-8'),(target_host, target_port))
print("Send Successful.")

# receive some data
data, addr = clint.recvfrom(4096)
print("Receive Successful.")

print(data.decode(), addr)

