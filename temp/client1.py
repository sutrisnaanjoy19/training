from ossaudiodev import SNDCTL_SEQ_NRSYNTHS
import socket
import sys
import json
import string
import random
import threading
import sys
from threading import Thread

class KVClient():
    def __init__(self, host: str, port: int, mode :str):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        while True:
            try:
                sock.connect((host, port))
                if mode == "stress":
                    t = Thread(target=self.printer_stress, args=((sock,)), daemon=True)
                    t.start()
                else:
                    t = Thread(target=self.printer_client, args=((sock,)), daemon=True)
                    t.start()
            except KeyboardInterrupt:
                break
        sock.close()

    def printer_client(self , sock ):
        try:
            print("\nFor adding element PUT <key> <value> \nFor deletion DEL <key> \nFor getting element GET <key> \nFor scanning the data SCAN \nFor exiting EXIT \n")
            while True:
                try:
                    sock.sendall(bytes(input(),encoding="utf-8"))
                    sock.recv(1024).decode("utf-8")
                except KeyboardInterrupt:
                    break
        finally:
            sock.close()

    def printer_stress(self , sock ):
        N = 2
        try:
            while True:
                res1 = ''.join(random.choices(string.ascii_lowercase + string.digits, k=N))
                res2 = ''.join(random.choices(string.ascii_lowercase + string.digits, k=N))
                msg1 = f"PUT {res1} {res2}"
                msg2 = f"GET {res1}"
                msg3 = f"DEL {res1}"
                try:
                    sock.sendall(bytes(msg1,encoding="utf-8"))
                    sock.sendall(bytes(msg2,encoding="utf-8"))
                    sock.sendall(bytes(msg3,encoding="utf-8"))
                    #print(sock.recv(1024).decode("utf-8"))
                except KeyboardInterrupt:
                    break

        finally:
            sock.close()

    
def stress_test():
    client = KVClient("localhost" , 9900 , "stress")

def main():
    print(sys.argv)
    count = int(sys.argv[1])
    for i in range(count):
        stress_test()
    if sys.argv[1] == None:
        client = KVClient("localhost" , 9900 , "client")


if __name__ == "__main__":
    main()












'''N = 2
HOST, PORT = "localhost", 9900

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def printer():
    while True:
        print(sock.recv(1024).decode("utf-8"))

try:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    t = Thread(target=printer, daemon=True)
    t.start()

finally:
    sock.close()
'''
 


