import socket
import math,time,secrets

HOST = "ackillin.net"
PORT = 45506
#USERNAME = input("Username? ")

def findPrimeFactors(nums,phi):
    while phi %2==0:
        nums.add(2)
        phi //= 2
    for i in range(3, int(math.sqrt(phi)),2):
        while phi%i == 0:
            #print(i)
            nums.add(i)
            phi = phi//i
    if phi > 2:
        nums.add(phi)

def cleaned_root(prime):
    nums = set()
    phi = prime-1
    findPrimeFactors(nums,phi)
    for num in range(2,phi+1):
        flag = False
        for factor in nums:
            if pow(num,phi//factor,prime) == 1:
                flag = True
                break
        if flag == False:
            return num
    return -1

def prim_root(prime):
    nums = set()
    final_set = []
    for test in range(prime,3,-1):
        #pow useage: base, exponent, modulo
        for x in range(1,prime-1):
            cur = pow(test,x,prime)
            if cur in nums:
                nums.clear()
                break
            else:
                nums.add(cur)
        if len(nums) > 0:
            final_set.append(test)
            if len(final_set) > 30:
                return secrets.choice(final_set)
        continue
    #print(f"Found a total of {len(final_set)}")
    print(f"Finished: {time.ctime()}")
    return secrets.choice(final_set)

def miller(num,d):
    #Rend below gets a positive int from 0 to num-4. We then add 2 to get rid of obviously non prime numbers
    a = secrets.randbelow(num-5) + 3
    x = pow(a,d,num)
    if x == 1 or x == num-1:
        return True
    #While we haven't gone to or past the prime, keep checking to see if its probably prime
    while d != num-1:
        x = (x*x) % num
        d *=2
        #x = pow(x,2,num)
        if x == 1:
            return False
        if x == num-1:
            return True
    return False

def is_prime(num,rounds):
    if num<=1 or num == 4:
        return False
    if num <=3:
        return True
    d = num-1
    while d %2 == 0:
        d //=2
    for i in range(rounds):
        if miller(num,d) == False:
            return False
    return True

def get_prime(bits):
    import secrets
    get_prime.prime = secrets.randbits(bits)
    while is_prime(get_prime.prime,rounds = 5) == False:
        get_prime.prime = secrets.randbits(bits)
        if get_prime.prime % 2 == 0:
            continue
    #Checks the number against 5 rounds of the miller test
    return get_prime.prime

def diffie(conn):
    #Send two public numbers (large prime, and a root prime)
    pass
def encoder(msg,key):
def decoder(msg,key):

def teehee():
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
if __name__ == "__main__":
    import sys
    #sys.setrecursionlimit(10000)
    print("Start: {}".format(time.ctime()))
    bits = 16
    #print(is_prime(359,5))
    primes = get_prime(bits)
    #print(primes)
    root = prim_root(primes)
    print(primes)
    print(root)
    #print(cleaned_root(int(input(" -> "))))
    print(f"Finished: {time.ctime()}")

