import socket

HOST = '192.168.100.226'
PORT = 9900

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))

socket.send('Hello'.encode('utf-8'))
print(socket.recv(1024))