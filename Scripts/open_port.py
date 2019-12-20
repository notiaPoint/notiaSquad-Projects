#!/usr/bin/python3

# Guilhem Mizrahi 12/2019
# this program opens 4 random ports in a specified range

import socket
import random
import threading

class portThread(threading.Thread):
    def __init__(self, port):
        threading.Thread.__init__(self)
        self.port = port

    def run(self):
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('', self.port))
        s.listen(1)
        while True:
            print("Listening on port", self.port)
            c, addr=s.accept()
            print("Connection from", addr)

def generate_port():
    return(random.randrange(1024, 2048))

if __name__=="__main__":
    ports = [generate_port() for i in range(4)]
    for port in ports:
        portThread(port).start()
