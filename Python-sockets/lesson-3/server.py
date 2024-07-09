import socket
import threading

HEADER = 64
FORMAT = 'utf8'

PORT = 1002
HOST = socket.gethostbyname(socket.gethostname())
ADDR = (HOST, PORT)

DISCONNECT = 'disconnect' 

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn, addr):
    print(f'New connection {addr} connected')
    
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            print(f'{addr}: {msg}')
            if msg == DISCONNECT:
                connected = False
                print(f'Connection {addr} disconnected')
    conn.close        


def start():
    server.listen(10)
    print(f'[server] listening on: {HOST}')
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f'Active threads {threading.activeCount() - 1} ')


print('[Starting] server')
start()