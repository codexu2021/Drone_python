import subprocess

arp = subprocess.run(['arp', '-a'], stdout=subprocess.PIPE, text=1)
arp_list = arp.stdout.splitlines()

for ip in arp_list:
  if ("1a:24:54:e6:ad" in ip):
    start = int(ip.find("(")) + 1
    end = int(ip.find(")"))
    print(ip[start:end])