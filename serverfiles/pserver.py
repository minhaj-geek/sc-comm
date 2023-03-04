import socket

# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

port = 9999

# bind the socket to a public host and a well-known port
serversocket.bind((host, port))

# become a server socket
serversocket.listen(1)

while True:
    # establish a connection
    clientsocket, addr = serversocket.accept()

    print("Got a connection from %s" % str(addr))

    message = 'Thank you for connecting' + "\r\n"
    clientsocket.send(message.encode('ascii'))

    # receive data from the client
    data = clientsocket.recv(1024).decode('ascii')
    print("Received from client: %s" % data)

    data = clientsocket.recv(1024).decode('ascii')
    print("Received from client: %s" % data)



    clientsocket.close()

