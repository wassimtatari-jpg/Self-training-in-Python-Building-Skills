import socket

server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_socket.bind(("localhost",5000))

server_socket.listen(5)

print("Connection progressing")

while True:
    clinet_server,client_adress=server_socket.accept()
    print(f"Connected with {client_adress}")
    while True:
        data=clinet_server.recv(1024)
        if not data:
            break
        message=data.decode('utf-8')
        if message=="exit":
            clinet_server.close()
            break
        else:
            clinet_server.sendall(b"Message Recived")