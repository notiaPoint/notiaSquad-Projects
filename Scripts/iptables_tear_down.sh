#!/bin/bash
# Restore the iptables rules to a fresh file allowing every connection
iptables-restore < /etc/iptables/rules.v4
