# -*- coding: utf-8 -*-

import socket, sys

host = 'localhost'
port = 50132
backlog = 5
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(('Socket created for: ' + host))

try:
    s.bind((host, port))
except socket.error as msg:
    print(('Bind failed. Error Code: ' + str(msg[0]) + ' Message ' + msg[1]))
    sys.exit()

print(("Socket has been binded to UDP Port: " + str(port)))

s.listen(backlog)
print("Socket now listening for connections...")

while True:
    client, address = s.accept()
    print((address[0] + ': has connected!'))
    data = client.recv(size)
    if data:
        client.send(data)
    client.close()