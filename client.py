import socket
import prims

HOST = "ackillin.net"
PORT = 45506
USERNAME = input("Username? ")

def diffie(conn,bits = 16):
    #Send two public numbers (large prime, and a root prime)
    #The client is considered "A" in this instance
    str_enc = lambda a: str(a).encode()
    prime,root = prims.get_both(bits)
    conn.send(str_enc(prime))
    conn.send(str_enc(root))

    #Second Round
    a = prims.get_random()
    #print(prime)
    #print(root)
    A = pow(prime,a,root)
    B = conn.recv(1024).decode()
    B = int(B)
    conn.send(str_enc(A))
    #print(A)
    #print(B)
    #print(a)
    #Finalize key
    key = pow(B,a,root)
    return key

def main_connection():
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        s.connect((HOST,PORT))
        key = diffie(s)
        print(key)
        s.sendall(prims.encoder(USERNAME,key))
        while True:
            data = s.recv(1024).decode()
            print (data)
            msg = input(" -> ")
            if msg != "exit":
                s.sendall(msg.encode())
            else:
                break
    print ("Broken off from server successfully")

if __name__ == "__main__":
    main_connection()

