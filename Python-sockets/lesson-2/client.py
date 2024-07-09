import socket

host = 'localhost'
port = 9990

client = socket.socket()
client.connect((host, port))

name = input('Enter name\n>>>')
client.send(name.encode('utf8'))

print(client.recv(1024).decode('utf-8'))