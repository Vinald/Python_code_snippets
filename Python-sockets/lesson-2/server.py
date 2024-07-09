import socket

host = 'localhost'
port = 9990

server = socket.socket()
print('Socket created')

server.bind((host, port))

server.listen(4)
print('waiting for connections')

while True:
    client, address = server.accept()
    name = client.recv(1024).decode('utf-8')
    print(f'connection established with {address} {name}')
        
    client.send('Welcome.'.encode('utf8'))
    client.close()