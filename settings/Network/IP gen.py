from pystyle import Center, Colorate, Colors, Anime
import colorama
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
                ┃ Discord: .gg/xxxxx  ┃
                ┗━━━━━━━━━━━━━━━━━━━━━┛
"""))

import requests
import json
import random
import subprocess
import sys
import threading
import concurrent.futures

colorama.init(autoreset=True)

def IpCheck():
    ip = ".".join(str(random.randint(1, 255)) for _ in range(4))
    
    try:
        if sys.platform.startswith("win"):
            result = subprocess.run(['ping', '-n', '1', ip], capture_output=True, text=True, timeout=0.1)
        elif sys.platform.startswith("linux"):
            result = subprocess.run(['ping', '-c', '1', '-W', '1', ip], capture_output=True, text=True, timeout=0.1)
        else:
            print(colorama.Fore.RED + "Unsupported platform.")
            return
        
        if result.returncode == 0:
            print(colorama.Fore.GREEN + f"[VALID] IP: {ip}")
        else:
            print(colorama.Fore.RED + f"[INVALID] IP: {ip}")

    except Exception:
        print(colorama.Fore.RED + f"[ERROR] IP: {ip}")

def Request(threads_number):
    try:
        with concurrent.futures.ThreadPoolExecutor(max_workers=threads_number) as executor:
            executor.map(lambda _: IpCheck(), range(threads_number))
    except Exception as e:
        print(colorama.Fore.RED + f"Error: {e}")

try:
    threads_number = int(input(colorama.Fore.CYAN + "Enter number of threads: "))
except ValueError:
    print(colorama.Fore.RED + "Invalid number.")
    exit()

while True:
    Request(threads_number)
