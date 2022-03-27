import socket


s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1025))
while True:
    msg=s.recv(1024)
    if (msg.decode("utf-8"))=="quit":
        s.close()
    print(msg.decode("utf-8"))
    b=input("enter message")

    s.send(bytes(b, "utf-8"))
    
    # b=input("enter text")
    # se=s.send(bytes(b, "utf-8"))