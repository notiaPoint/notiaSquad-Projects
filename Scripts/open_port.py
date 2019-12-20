#!/usr/bin/python3

# Guilhem Mizrahi 09/2019
# this program opens a specific port

import socket
import random
import threading

class portThread(threading.Thread):
    def __init__(self, port):
        threading.Thread.__init__(self)
        self.port = port

    def run(self):
        print("Opening port {}".format(self.port))
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('127.0.0.1', self.port))
        s.listen(1)
        while True:
            print("Listening on port", self.port)
            c, addr=s.accept()
            print("Connection from", addr)

def generate_port():
    return(random.randrange(10000, 20000))

# def open_port(port_number):
#     s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     s.bind(('0.0.0.0', port_number))
#     s.listen(1)
#     while True:
#         print("Listening on port", port_number)
#         c, addr=s.accept()
#         print("Connection from", addr)
#         print("Closing")
#         # s.close()
#         # break
#     s.exit()

if __name__=="__main__":
    ports = [generate_port() for i in range(4)]
    # print(ports)
    for port in ports:
        # _thread.start_new_thread(open_port, (port,))
        portThread(port).start()
    # open_port(10000)
