#!/bin/bash

# Guilhem Mizrahi
# 12/2019

# Restore the iptables rules to a fresh file allowing every connection

function reset_iptables(){
	# First check if the user is root
	if [[ $EUID -ne 0 ]]
	then
		echo "Permission denied. Script must be run as root";
		exit 1;
	else
				# restore the iptables from a fresh file
        iptables-restore < rules.v4;
		return 0;
	fi
}

# call the function
reset_iptables;
