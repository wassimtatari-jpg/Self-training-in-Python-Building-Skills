import socket

socket_server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

socket_server.bind(("localhost",5000))


socket_server.listen(4)

print("Waiting for connection")

while True:
    client_socket,client_adress=socket_server.accept()
    print(f"Conncted with {client_adress}")
    data=client_socket.recv(1024)
    print(f"Data recived {data.decode('utf-8')}")
    client_socket.sendall(b"hello")
    client_socket.close()
