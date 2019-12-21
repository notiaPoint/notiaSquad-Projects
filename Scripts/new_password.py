#!/usr/bin/python3

# Guilhem Mizrahi
# 12/2019

import random
import os

def select_password():
    """
    Select a random password from the file top100.txt
    These passwords are weak and can be broken by Hydra
    """
    top100 = open("../top100.txt", "r")
    lines = top100.readlines()
    new_pass = random.choice(lines).strip()
    # print(new_pass)
    return(new_pass)

def main():
    """
    Print the command to type to change password
    """
    new_pass = select_password()
    print("Your new password is", new_pass)
    print("")
    print("Execute the command bellow to update it")
    command = "echo -e \""+new_pass+"\\n"+new_pass+"\""+" | passwd"
    print(command)

if __name__ == '__main__':
    main()
