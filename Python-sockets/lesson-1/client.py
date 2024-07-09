import socket

HOST = '192.168.100.19'
PORT = 9090

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))

socket.send('Hello'.encode('utf8'))
print(socket.recv(1024))