
import socket

# create a socket object
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
#host = socket.gethostname()
host ="10.2.16.173"
port = 9999

# connection to hostname on the port.
clientsocket.connect((host, port))

# send a thank you message to the client
message = 'Thank you for connecting' + "\r\n"
clientsocket.send(message.encode('ascii'))

# receive data from the server
data = clientsocket.recv(1024).decode('ascii')
print("Received from server: %s" % data)

# send some data to the server
message = 'Hello server, how are you?' + "\r\n"
clientsocket.send(message.encode('ascii'))

clientsocket.close()
