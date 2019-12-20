#!/usr/bin/python3

import random
import subprocess
import os

def generate_port():
    return(random.randrange(10000, 20000))

def change_ssh_config(port):
    #subprocess.run(["sed", "-i", "/Port/c\\Port "+str(port), "/etc/ssh/ssh_config"])
    subprocess.run(["sed", "-i", "/Port/c\\Port "+str(port), "/etc/ssh/sshd_config"])
    #subprocess.run(["systemctl", "restart", "sshd"])

def main():
    if os.geteuid()==0:
        port = generate_port()
        change_ssh_config(port)
        subprocess.run(["systemctl", "restart", "sshd"])
    else:
        print("Permission denied.")

if __name__=="__main__":
    main()
