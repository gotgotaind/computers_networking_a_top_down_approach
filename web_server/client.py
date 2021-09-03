
from socket import *
import sys

def create_client_socket(servername,port):
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect((servername,port))
    return client_socket



def main(argv):
    servername=argv[1]
    port=int(argv[2])
    print(f'Creating client socket connecting to {servername}:{port}')
    client_socket=create_client_socket(servername,port)

    file=argv[3]
    print(f'Asking for {file}')
    request_line=f'GET /{file} HTTP/1.1\r\n'
    client_socket.send(request_line.encode())

    
    while(True):
        server_reply = client_socket.recv(1024)
        if( not server_reply ):
            break
        print(f'Server replied: {server_reply.decode()}')

    client_socket.close()

if __name__ == "__main__":
    # execute only if run as a script
    main(sys.argv)