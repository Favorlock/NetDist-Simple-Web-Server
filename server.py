# import socket module
from socket import *
import sys  # In order to terminate the program

host = '0.0.0.0'
port = 8080

print(host + ':' + str(port))

serverSocket = socket(AF_INET, SOCK_STREAM)
# Prepare a sever socket
serverSocket.bind((host, port))
serverSocket.listen(5)
while True:
    # Establish the connection
    print('Ready to serve...')
    (client, addr) = serverSocket.accept()
    try:
        raw = client.recv(1024).decode()
        if not raw:
            continue
        request = raw.split()[1]
        f = open(request[1:], 'rb')

        header = 'HTTP/1.1 200 OK\n\n'
        data = f.read()
        # Send one HTTP header line into socket
        # Send the content of the requested file to the client
        client.send(header.encode())
        client.send(data)
        client.send('\r\n'.encode())
    except IOError:
        # Send response message for file not found
        header = 'HTTP/1.1 404 Not Found\n\n'
        data = '<html><body><h1>404 NOT FOUND</h1></body></html>'
        client.send(header.encode())
        client.send(data.encode())
        client.send('\r\n'.encode())
    # Close client socket
    client.close()
serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data
