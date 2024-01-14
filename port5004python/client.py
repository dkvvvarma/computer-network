import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 5004
client_socket.connect((host, port))
print("Connected to {}:{}".format(host, port))
while True:
    message = input("Client: ")
    client_socket.send(message.encode())
    if message == "bye":
        break
    data = client_socket.recv(1024).decode()
    print("Server: {}".format(data))
client_socket.close()
