import socket

HOST = '192.168.100.19'
PORT = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen(5)

while True:
    communication_socket, address = server.accept()
    print(f'connected to {address}')
    message = communication_socket.recv(1024).decode('utf8')
    print(f'client: {message}')
    communication_socket.send(f'Got your message'.encode('utf8'))
    communication_socket.close()
    print('disconnected') 