#!/usr/bin/python3

# Guilhem Mizrahi 12/2019
# this program opens 4 random ports in a specified range

import socket           # to open the ports
import random           # to choose random ports
import threading        # to allow for multiple ports at the same time

class portThread(threading.Thread):
    """
    Class to implement a listener on a port
    """
    def __init__(self, port):
        """
        Initialize the object with the specified port number
        """
        threading.Thread.__init__(self)
        self.port = port

    def run(self):
        """
        Start the listener on the port associated with the thread
        """
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('', self.port))
        s.listen(1)
        while True:
            print("Listening on port", self.port)
            c, addr=s.accept()
            print("Connection from", addr)

def generate_port():
    """
    Choose a random number in the range 1024-2048 to assign to ports
    """
    return(random.randrange(1024, 2048))

def main():
    """
    Generate 5 random numbers and open listeners on the corresponding ports
    """
    ports = [generate_port() for i in range(5)]
    for port in ports:
        portThread(port).start()

if __name__=="__main__":
    main()
