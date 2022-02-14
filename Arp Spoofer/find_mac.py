import sys
import scapy.all as scapy
from colorama import Fore

target_ip = input(b"Enter The Target Ip Address: ")
def mac(ip):
    arp_req = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")/arp_req
    res = scapy.srp(broadcast, timeout=1 , verbose=False)[0]
    arp_req.show
    arp_req.summary()
    print(Fore.RED,"[*]The Target IP Address is : ",ip)
    print(Fore.YELLOW,"[+]The Target Mac Found!: ",res[0][1].hwsrc)

mac(target_ip)
