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
| $$  \ $$| $$      | $$      | $$  | $$| $$  \ $$| $$  | $$
| $$$$$$$/| $$$$$$$$| $$$$$$$$|  $$$$$$/|  $$$$$$/| $$  | $$
|_______/ |________/|________/ \______/  \______/ |__/  |__/

                ┏━━━━━━━━━━━━━━━━━━━━━┓
                ┃  Author : Ego/xhe   ┃
                ┃ Discord: .gg/xxxx   ┃
                ┗━━━━━━━━━━━━━━━━━━━━━┛
                          
"""))
import requests

def domain_scanner(domain, directories):
    subdomains = [
        "mail", "mail2", "www", "ns2", "ns1", "blog", "localhost", "m", "ftp", "mobile", "ns3",
        "smtp", "search", "api", "dev", "secure", "webmail", "admin", "img", "news", "sms",
        "marketing", "test", "video", "www2", "media", "static", "ads", "beta", "wap", "blogs",
        "download", "dns1", "www3", "origin", "shop", "forum", "chat", "www1", "image", "new",
        "tv", "dns", "services", "music", "images", "pay", "ddrint", "conc"
    ]

    print('URLS FOUND:')
    
    for sub in subdomains:
        full_domain = f"{sub}.{domain}"
        for directory in directories:
            url = f"https://{full_domain}/{directory}"
            try:
                response = requests.get(url, timeout=3)
                if response.status_code == 200:
                    print(f'[+] {url}')
            except requests.RequestException:
                pass

domain = input("Enter the Domain Name: ")

directories = [
    "", "admin", "login", "dashboard", "api", "images", "uploads", "home",
    "index", "test", "backup", "old", "v1", "v2", "private", "config", "data",
    "js", "css", "files", "secure", "hidden", "panel"
]

domain_scanner(domain, directories)
input(" ")