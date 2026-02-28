from scapy.all import sniff, IP, UDP
import subprocess
import os
from pystyle import Center, Colorate, Colors, Anime
from colorama import Fore

os.system('cls')
print(Colorate.Horizontal(Colors.blue_to_cyan,"""
 /$$$$$$$  /$$$$$$$$ /$$       /$$   /$$  /$$$$$$   /$$$$$$ 
| $$__  $$| $$_____/| $$      | $$  | $$ /$$__  $$ /$$__  $$
| $$  \ $$| $$      | $$      | $$  | $$| $$  \__/| $$  \ $$
| $$$$$$$ | $$$$$   | $$      | $$  | $$| $$ /$$$$| $$$$$$$$
| $$__  $$| $$__/   | $$      | $$  | $$| $$|_  $$| $$__  $$
| $$  \ $$| $$      | $$      | $$  | $$| $$  \ $$| $$  | $$
| $$$$$$$/| $$$$$$$$| $$$$$$$$|  $$$$$$/|  $$$$$$/| $$  | $$
|_______/ |________/|________/ \______/  \______/ |__/  |__/

                ┏━━━━━━━━━━━━━━━━━━━━━┓
                ┃  Author : Ego/xhe   ┃
                ┃ Discord: .gg/xxxx   ┃
                ┗━━━━━━━━━━━━━━━━━━━━━┛
                          
"""))


def packet_handler(packet):
    if packet.haslayer(IP) and packet.haslayer(UDP):
        source_ip = packet[IP].src
        dest_ip = packet[IP].dst
        source_port = packet[UDP].sport
        dest_port = packet[UDP].dport

        fortnite_ports = [7777, 7778, 7788] + list(range(9000, 9101))
        if dest_port in fortnite_ports:
            payload = packet[UDP].payload
            print(f"Fortnite IP Sniffed {source_ip}:{source_port} to {dest_ip}:{dest_port}: {payload}")

def sniff_fortnite_traffic():
    print(Fore.CYAN + "Sniffing...")
    sniff(filter="udp and ip", prn=packet_handler)

input(Fore.BLUE + "Press Enter to start sniffing Fortnite IP traffic...")
sniff_fortnite_traffic()
input(Fore.RED + "Press enter to exit...")