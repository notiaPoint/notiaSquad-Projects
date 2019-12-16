import subprocess

def tear_down(backup_file):
    #sudo iptables-restore < /etc/iptables/rules.v4
    subprocess.call(["iptables-restore", stdin=open(backup_file, "r")])

def main(backup_file):
    tear_down(backup_file)

if __name__=="__main__":
    backup_file = "~/Documents/Notia/rules.v4"
    main(backup_file)
