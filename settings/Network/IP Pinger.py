from pystyle import Center, Colorate, Colors, Anime
import colorama
import os
import socket
import time
import concurrent.futures

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

colorama.init(autoreset=True)

def ping_ip(hostname, port, packet_size):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(2)
            start_time = time.time()
            sock.connect((hostname, port))
            data = b'\x00' * packet_size
            sock.sendall(data)
            elapsed_time = (time.time() - start_time) * 1000
            print(colorama.Fore.GREEN + f"[+] {hostname} | {elapsed_time:.2f}ms | Port: {port} | Bytes: {packet_size} | Status: Success")
    except:
        print(colorama.Fore.RED + f"[-] {hostname} | Port: {port} | Bytes: {packet_size} | Status: Failed")

try:
    hostname = input(colorama.Fore.CYAN + "Enter IP: ")

    port_input = input(colorama.Fore.CYAN + "Enter Port (default 80): ")
    port = int(port_input) if port_input else 80

    bytes_input = input(colorama.Fore.CYAN + "Enter Packet Size (default 64): ")
    packet_size = int(bytes_input) if bytes_input else 64

    with concurrent.futures.ThreadPoolExecutor() as executor:
        while True:
            time.sleep(0.1)
            executor.submit(ping_ip, hostname, port, packet_size)

except Exception as e:
    print(colorama.Fore.RED + f"Error: {e}")
