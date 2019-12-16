import random
import subprocess
import sys

def generate_port():
    return(random.randrange(10000, 20000))

def change_ssh_config(port):
    #subprocess.run(["sed", "-i", "/Port/c\\Port "+str(port), "/etc/ssh/ssh_config"])
    subprocess.run(["sed", "-i", "/Port/c\\Port "+str(port), "/etc/ssh/sshd_config"])
    #subprocess.run(["systemctl", "restart", "sshd"])

def main():
    port = generate_port()
    change_ssh_config(port)

if __name__=="__main__":
    main()
