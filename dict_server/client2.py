import socket
import sys
import json
import time
import string
import random
from threading import Thread
global start , end
N = 2
HOST, PORT = "localhost", 9900

def client(count:int,):
# Create a socket (SOCK_STREAM means a TCP socket)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #def printer():
   #     while True:
   #         print(sock.recv(1024).decode("utf-8"))

    try:
        # Connect to server and send data
        sock.connect((HOST, PORT))
        #t = Thread(target=printer, daemon=True)
        #t.start()
        for i in range(count):
            res1 = ''.join(random.choices(string.ascii_lowercase + string.digits, k=N))
            res2 = ''.join(random.choices(string.ascii_lowercase + string.digits, k=N))
            msg1 = f"PUT {res1} {res2}"
            msg2 = f"GET {res1}"
            msg3 = f"DEL {res1}"
            try:
                sock.sendall(bytes(msg1,encoding="utf-8"))
                print(sock.recv(1024).decode("utf-8"))
                sock.sendall(bytes(msg2,encoding="utf-8"))
                print(sock.recv(1024).decode("utf-8"))
                sock.sendall(bytes(msg3,encoding="utf-8"))
                print(sock.recv(1024).decode("utf-8"))
                
                # print(msg1,msg2,msg3)
            except KeyboardInterrupt:
                break
    finally:
        sock.close()
        


def main():
    start = time.time()
    threads = []
    for i in range(int(sys.argv[1])):
        t = Thread(target=client, args=((int(sys.argv[1]),)))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
    end = time.time()
    print(end-start)

if __name__ == "__main__":
    main()
