#!/usr/bin/python3

# Guilhem Mizrahi
# 12/2019

import os
import subprocess
import time

def ping_list(ip_list, point_list):
    """
    ping each ip in the list and count how many times they respond
    """
    while True:
        for i in range(len(ip_list)):
            # res = os.system("ping -c1 "+ip_list[i]+" 2>&1 >/dev/null")
            res = subprocess.call("ping"+" -c1"+" -t2 "+ip_list[i]+" 2>&1 >/dev/null", shell=True)
            if res == 0:
                point_list[i] += 1
            else:
                print(ip_list[i], "is down")
        print([(ip_list[i], point_list[i]) for i in range(len(ip_list))])
        # time.sleep(5)

def main(ip_list):
    point_list = [0]*len(ip_list)
    ping_list(ip_list, point_list)

if __name__ == '__main__':
    ip_list = ["10.0.3.236", "10.0.3.212"]
    main(ip_list)
