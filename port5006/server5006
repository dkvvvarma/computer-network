import socket
server = socket.socket()
server.bind(("localhost",5006))
server.listen(3)
print("Server Activated")
while True:
    client,address = server.accept()
    print(str(address)+"is connected.")
    client_request=client.recv(1024)
    print("Server received",client_request)
    filename=client_request
    f=open(filename,'rb')
    I=f.read(1024)
    socket.close.send(I)
    f.close()
    print("FIle Sent to"+str(address)+"server!")