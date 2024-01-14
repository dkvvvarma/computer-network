import socket
import threading

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('localhost', 59))
    
    while True:
        data, address = server_socket.recvfrom(1024)
        t = threading.Thread(target=serve_client, args=(server_socket, address, data))
        t.start()

def serve_client(server_socket, address, data):
    filename = data.decode()
    try:
        with open(filename, 'rb') f:
            file_data = f.read()
            server_socket.sendto(file_data, address)
    except FileNotFoundError:
        server_socket.sendto(b'File not found', address)

if __name__ == '__main__':
    server()

