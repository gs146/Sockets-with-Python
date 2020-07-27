import socket

#AF_INET is used for IPv4 and SOCK_STREAM is a TCP algo for connection
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#binding to socket, tuple is given of size 2 containing host and port on that
s.bind((socket.gethostname(),1235))  #IP and port

#5 is given to handle more than one connection 
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Connection from{address} has been established!")
    clientsocket.send(bytes("Welcome to the server! This is me Gaurav Sharma.", "utf-8"))
    clientsocket.close()
