import socket

client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client_socket.connect(("localhost",5000))

client_socket.sendall(b"helo Server")

data=client_socket.recv(1024)
print(f"data recived {data.decode('utf-8')}")

client_socket.close()