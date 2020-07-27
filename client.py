import socket

#AF_INET is used for IPv4 and SOCK_STREAM is a TCP algo for connection
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(),1235))

# msg = s.recv(1024)
# print(msg.decode("utf-8"))
full_msg = ""
while True:
    msg = s.recv(8)
    if(len(msg)>0):
        full_msg+=msg.decode("utf-8")
    else:
        break

print(full_msg)
