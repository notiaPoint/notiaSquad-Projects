Once you've found the hosts you're going to attack you will next go through and use TCHydra to brute force the ssh login on the machine.

1. Hydra will come pre configured on each machine.
2. Each round there will be a new password set for the account we wil brute force the ssh login on. We will use a top 1000 passwords word list and inject this into the login.
3. by running the following command we will iniate the attack.

hydra -s "port number" -l root -P "location of wordlist" "IP Address" -t 4 -V ssh

4. The first flag -s allows us to input the ssh port number into the program. The flag -l tells the hydra command what user we are trying to brute force the login on. Next, the -P flag will let us pass the absolute path to the word list we will use. We then input the IP address we are trying to brute forcce. The -t flag is how many threads per attempt, we will set it at 4 because this is what hydra suggests for attacking ssh. Finally the -V flag controls the verbosity and shows us whats being run, and the ssh after is telling the program we are doing this attack on an ssh login.

5. After the attack is done, you will be granted with a success message and a user name and password to go ahead a login to the compromised machine with. 
