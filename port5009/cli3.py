from socket import *
host = '127.0.0.1'
port = 5009
client_soc = socket(AF_INET,SOCK_DGRAM)
file_name = input("Enter file name req : ")
client_soc.sendto(file_name.encode(),(host,port))
file,server_adrs = client_soc.recvfrom(1024)
file = file.decode()
if file == '':
    print("Empty file")
else :
    print(file)
client_soc.close()