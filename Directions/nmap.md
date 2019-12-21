Here we will explain the steps for doing the nmap scan.

1. Determine subnet that needs to be scanned, this will either be provided by instructors with a range of IP's or with our pre-configured network.

2. run nmap command as follows and find open ports on IP's

nmap -sV 192.168.1.0/24 -T5 -p1024-2048

3. the -sV flag will enable version Detection using a TCP/IP stack fingerprint, and the -T5 flag will give a faster than default scan speed and the -p flag will specify to scan all the ports instead of the top 1000 well known ports.

4. Once you run the scan you will come up with a list of IP's and what ports are open and what services are on those ports.
