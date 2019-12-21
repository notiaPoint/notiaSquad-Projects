#!/usr/bin/python3

# Guilhem Mizrahi
# 12/2019

import random
import os

def select_password():
    """
    Select a random password from the file top100.txt
    """
    top100 = open("../top100.txt", "r")
    lines = top100.readlines()
    new_pass = random.choice(lines).strip()
    # print(new_pass)
    return(new_pass)

def main():
    """
    Check if user is root
    """
    if os.geteuid()==0:
        new_pass = select_password()
        command = "echo \""+new_pass+"\n"+new_pass+"\""+" | passwd"
        print(command)
    else:
        raise PermissionError("Permission denied for user with UID {}".format(os.geteuid()))

if __name__ == '__main__':
    main()
