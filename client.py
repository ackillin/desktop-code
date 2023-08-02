import socket

HOST = "ackillin.net"
PORT = 45506
USERNAME = input("Username? ")
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    s.sendall(USERNAME.encode())
    while True:
        data = s.recv(1024).decode()
        print (data)
        msg = input(" -> ")
        if msg != "exit":
            s.sendall(msg.encode())
        else:
            break
print ("Broken off from server successfully")
