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
                ┃ Discord: .gg/xxxx   ┃
                ┗━━━━━━━━━━━━━━━━━━━━━┛
"""))

import socket
import ssl
import subprocess
import sys
import requests
import concurrent.futures

colorama.init(autoreset=True)

def IpType(ip):
    ip_type = "IPv6" if ':' in ip else "IPv4" if '.' in ip else "Unknown"
    print(colorama.Fore.CYAN + f"IP Type: {ip_type}")

def IpPing(ip):
    try:
        ping_cmd = ['ping', '-n', '1', ip] if sys.platform.startswith("win") else ['ping', '-c', '1', '-W', '1', ip]
        result = subprocess.run(ping_cmd, capture_output=True, text=True, timeout=1)
        status = "Succeed" if result.returncode == 0 else "Fail"
    except Exception:
        status = "Fail"
    print(colorama.Fore.YELLOW + f"Ping: {status}")

def IpPort(ip):
    ports = {
        21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS",
        80: "HTTP", 110: "POP3", 443: "HTTPS", 3306: "MySQL", 3389: "RDP"
    }

    def scan(port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            if sock.connect_ex((ip, port)) == 0:
                print(colorama.Fore.GREEN + f"Port {port} Open - {ports.get(port, 'Unknown')}")

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(scan, ports.keys())

def IpDns(ip):
    try:
        dns = socket.gethostbyaddr(ip)[0]
    except Exception:
        dns = "None"
    print(colorama.Fore.MAGENTA + f"DNS: {dns}")

def IpHostInfo(ip):
    try:
        data = requests.get(f"https://ipinfo.io/{ip}/json").json()
        print(colorama.Fore.BLUE + f"Country: {data.get('country', 'Unknown')}")
        print(colorama.Fore.BLUE + f"ISP: {data.get('org', 'Unknown')}")
    except requests.RequestException:
        print(colorama.Fore.RED + "Host Info Not Available")

def SslCertificateCheck(ip):
    try:
        with socket.create_connection((ip, 443), timeout=1) as sock:
            context = ssl.create_default_context()
            with context.wrap_socket(sock, server_hostname=ip) as ssock:
                cert = ssock.getpeercert()
                print(colorama.Fore.CYAN + f"SSL Certificate: {cert}")
    except Exception as e:
        print(colorama.Fore.RED + f"SSL Certificate Check Failed: {e}")

try:
    ip = input(colorama.Fore.WHITE + "Enter IP: ")
    print(colorama.Fore.YELLOW + "Fetching Information...")
    IpType(ip)
    IpPing(ip)
    IpDns(ip)
    IpPort(ip)
    IpHostInfo(ip)
    SslCertificateCheck(ip)
except Exception as e:
    print(colorama.Fore.RED + f"Error: {e}")
