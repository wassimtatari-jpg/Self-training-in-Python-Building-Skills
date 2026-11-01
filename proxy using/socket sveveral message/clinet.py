import socket

client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client_socket.connect(("localhost",5000))

while True:
    user_message=input("Enter your message:")
    client_socket.sendall(user_message.encode('utf-8'))
    if user_message.lower().strip()=="exit":
        client_socket.close()
        print("Connection closed")
        break
    else:
        data=client_socket.recv(1024)
        print(f"Recived data {data.decode('utf-8')}")
