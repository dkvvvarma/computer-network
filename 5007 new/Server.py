# Server Program
import socket
port=5007
s=socket.socket()
host=socket.gethostname()
s.bind((host,port))
s.listen(5)
print('Server is listening....')
while True:
 conn,addr=s.accept()
 print('Got connection from',addr)
 data=conn.recv(1024)
print('Server received',data)
  filename=data
 f=open(filename,'rb')
 l=f.read(1024)
while(l):
conn.send(l)
3
print('Sent',repr(l))
 l=f.read(1024)
f.close
print('Done sending' )
conn.close()