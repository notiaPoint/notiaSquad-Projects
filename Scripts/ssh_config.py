#!/usr/bin/python3

# Guilhem Mizrahi 12/2019
# Change the port for ssh and asign it to a random port in the range 1024-2048

import random
import subprocess
import os

def generate_port():
    """
    Return a random integer in the range 1024-2048. This value will be assigned to SSH
    """
    return(random.randrange(1024, 2048))

def change_ssh_config(port):
    """
    Change the port for SSH
    """
    subprocess.run(["sed", "-i", "/Port/c\\Port "+str(port), "/etc/ssh/sshd_config"])

def main():
    """
    Check if user is root
    """
    if os.geteuid()==0:
        port = generate_port()
        change_ssh_config(port)
        subprocess.run(["systemctl", "restart", "ssh"])
    else:
        raise PermissionError("Permission denied for user with UID {}".format(os.geteuid()))

if __name__=="__main__":
    main()
