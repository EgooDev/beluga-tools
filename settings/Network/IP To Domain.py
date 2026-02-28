from pystyle import Center, Colorate, Colors, Anime
from colorama import Fore
import os
import socket

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
def iptodomain():
    ip = input(Fore.BLUE + 'Type IP: ' + Fore.WHITE)
    if (ip == ''):
        return
    try:
        domain = socket.gethostbyaddr(ip)[0]
    except (socket.herror, socket.gaierror):
        try:
            domain = socket.gethostbyaddr(socket.gethostbyname(socket.gethostbyaddr(ip)[0]))[0]
        except (socket.herror, socket.gaierror):
            print(Fore.RED + 'No domain associated with this IP.')
    print('\n\u001b[34m[\u001b[37m+\u001b[34m] \u001b[37mDomain: ' + domain)

iptodomain()
input(Fore.RED + "Press enter to exit...")