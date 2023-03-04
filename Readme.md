This project is to make a server listen on a specified port for incoming connections, while the client connects to the server and sends and receives text messages.
 
* Download serverfiles directory on machine that you want to work as server and download clientfiles directory on machine that you want to work as client. 

1. You will find a python file(pserver.py) inside serverfiles directory. Execute this python file using command [python3 pserver.py] on one machine. 

2. You will find a python file(pcaller.py) inside clientfiles directory. Execute this python file using command [python3 pcaller.py] on other machine.
  2.1 Inside pclient.py file there will be line which will be defining host/server. if the server and client aren't same then you must set host manually.
      host="<your server ip>" 
      Example: host="1.1.2.4"

Note: The server and client could be one machine. 
