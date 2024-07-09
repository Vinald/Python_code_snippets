import socket

HOST = '192.168.100.226'

PORT = 9900

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen(5)

while True:
    communication_socket, aaddress = server.accept()
    print(f'connected to {aaddress}')
    message = communication_socket.recv(1024).decode('utf-8')
    print(f'client message {message}')
    communication_socket.send(f'Got message'.encode('utf-8'))
    communication_socket.close()
    print(f'connection with {aaddress} ended.').decode('utf-8')
