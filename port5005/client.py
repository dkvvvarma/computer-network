import socket

def client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    filename = input('Enter filename: ')
    client_socket.sendto(filename.encode(), ('localhost', 59))
    file_data, server_address = client_socket.recvfrom(1024)
    print(file_data.decode())

if __name__ == '__main__':
    client()

#make a text file with text1