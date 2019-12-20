#!/bin/bash
# Restore the iptables rules to a fresh file allowing every connection

function reset_iptables(){
	if [[ $EUID -ne 0 ]]
	then
		echo "Permission denied. Script must be run as root";
		exit 1;
	else
        iptables-restore < rules.v4;
		return 0;
	fi
}

reset_iptables;
