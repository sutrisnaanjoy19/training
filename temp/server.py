import socket
import sys
import json
import os
import threading
from _thread import *

HOST, PORT = "localhost", 12345
print_lock = threading.Lock()

data = json.load(open("file.json" , 'r'))
print(data)

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST , PORT))
sock.listen(100)

def threaded(c):
    global data
    while True:
        # data received from client
        c.sendall(bytes(json.dumps(data),encoding="utf-8"))
        # Receive data from the server and shut down
        received = c.recv(4096)
        received = received.decode("utf-8")
        data = json.loads(received)
    # connection closed
    c.close()

while True:
        # Connect to server and send data
        c , addr = sock.accept()
        # print_lock.acquire()
        #print(c)
        t= threading.Thread(target=threaded , args=[c,], daemon=True)
        t.start()
        #start_new_thread(threaded, (c,))

#c.close()
print("some exception has occured ")

#print(f"Sent: {data}")
#recv = json.loads(received)received = c.recv(4096)
print(f"Received: {data}")

with open("/home/sutrisna/Desktop/pypy/file.json", "w") as outfile:
        json.dump(recv, outfile)


