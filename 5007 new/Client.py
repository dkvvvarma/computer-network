import socket
s=socket.socket()
host=socket.gethostname()
port=5007
s.connect((host,port))
s.send('First File.txt'.encode())
with open('recieved_file.txt','wb') as f:
 print('file opened')
while True:
 data=s.recv(1024).decode()
if not data:
 break
print('recieving data...')
print('data in recieved file:')
print(data)
f.write(data.encode())
f.close()
print('Successfully got the first file')
s.close()
print('connection closed')