from socket import *
host = "127.0.0.1"
port = 5009
server_soc = socket(AF_INET,SOCK_DGRAM)
server_soc.bind((host,port))
print("Server is ready to listen")
n = int(input("Enter the number of clients : "))
for i in range(n):
    file_name,client_adrs = server_soc.recvfrom(1024)
    print('Client',i+1,'-',file_name.decode())
    try:
        f = open(file_name.decode(),"rb")
        l = f.read()
        server_soc.sendto(l,client_adrs)
        print("The file has been sent to client",i+1)
        f.close()
    except:
        msg = "the file is not present"
        server_soc.sendto(mgs.encode(),client_adrs)

  #bin