import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 5004
server_socket.bind((host, port))
server_socket.listen(1)
print("Server is running on {}:{}".format(host, port))
client_socket, address = server_socket.accept()
print("Got connection from {}".format(address))
while True:
    data = client_socket.recv(1024).decode()
    print("Client: {}".format(data))
    message = input("Server: ")
    client_socket.send(message.encode())
    if message == "bye":
        break
client_sot.close()
server_socket.close()
