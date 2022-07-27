#import KVServer
import json
import socket
import threading
from time import sleep
import http.server
import time
import logging
from functools import wraps
from prometheus_client import Counter, Histogram
from prometheus_client import start_http_server, Summary

REQUEST_COUNT = Counter('request_count','description')
#REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')


class KVServer():
    def __init__(self, host: str, port: int):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((host, port))
        sock.listen(100)
        self.read()
        while True:
            try:
                c , addr = sock.accept()
                print("accept conn")
                t= threading.Thread(target=self.threaded , args=[c,], daemon=True)
                t.start()
            except KeyboardInterrupt:
                break
        sock.close()

    #@REQUEST_TIME.time()

    def threaded(self, c): 
        while True:
            REQUEST_COUNT.inc()
            sleep(0.5)
            #c.sendall(bytes("\nFor adding element PUT <key> <value> \nFor deletion DEL <key> \nFor getting element GET <key> \nFor scanning the data SCAN \nFor exiting EXIT \n",encoding="utf-8"))
            received = c.recv(4096)
            received = received.decode("utf-8")
            #print(f"request from clients: {received}")
            if "PUT" in received:
                string=received.split()
                self.PUT(string[1], string[2])
                print("PUT")
                c.sendall(bytes("Done", encoding="utf-8"))
            elif "GET" in received:
                string=received.split()
                msg = self.GET(string[1])
                c.sendall(bytes(msg, encoding="utf-8"))
            elif "DEL" in received:
                string=received.split()
                self.DEL(string[1])
                c.sendall(bytes("Done", encoding="utf-8"))
            elif "SCAN" in received:
                c.sendall(bytes(json.dumps(self.data),encoding="utf-8"))
            else: c.close()


    def read(self):
        self.data = json.load(open("file.json", 'r'))

    def GET(self, key: str):
        try:
            value_for_specific_key = self.data[key]
            return value_for_specific_key
        except:
            return "key is not present"
        #raise NotImplementedError

    def PUT(self, key: str, value: str):
        """calls the server and returns the value of `key`"""
        #raise NotImplementedError
        self.data[key] = value

    def DEL(self , key: str):
        ''' comments '''
        try:
            del self.data[key]
            return "Done"
        except:
            return "key is not present"

    def scan(self):
        """
        implement an iterator that lists the entire contents of the
        remote kvstore
        """
        with open("/home/sutrisna/Desktop/pypy/file.json", "w") as outfile:
            json.dump(self.data, outfile)
        #print(self.data)
        return(self.data)

def main():    
    start_http_server(8000)
    server = KVServer('localhost', port=9900)

if __name__ == "__main__":
    main()