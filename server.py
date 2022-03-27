from logging.config import listen
import socket

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1025))
s.listen(5)
clt, adr=s.accept()
while True:
    a=input("enter text")
    clt.send(bytes(a, "utf-8"))
    msg=clt.recv(1024)
    print(msg.decode("utf-8"))
    
    # msg=s.recv(1024)
    # print(msg.decode("utf-8"))