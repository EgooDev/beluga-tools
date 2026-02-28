import requests
import colorama
from colorama import Fore
import os
import subprocess
import time
import webbrowser

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

def get_ip_info(ip):
    url_ip_api = f'http://ip-api.com/json/{ip}'
    url_ip_info = f'https://ipinfo.io/{ip}/json'
    

    response_api = requests.get(url_ip_api)
    info_api = response_api.json() if response_api.status_code == 200 else None
    

    response_info = requests.get(url_ip_info)
    info_info = response_info.json() if response_info.status_code == 200 else None

    return info_api, info_info

def get_ip_info2():
    ip = input(Fore.CYAN + "IP : " + Fore.BLUE)
    info_api, info_info = get_ip_info(ip)
    print(Fore.WHITE + " ")
    if info_api and info_api['status'] == 'success':
        print(Fore.CYAN + f"Informations de {ip} via API:")
        print(Fore.WHITE + f"Ville : {info_api.get('city', 'Inconnu')}")
        print(f"Région : {info_api.get('regionName', 'Inconnu')}")
        print(f"Pays : {info_api.get('country', 'Inconnu')}")
        print(f"Code postal : {info_api.get('zip', 'Inconnu')}")
        print(f"Latitude : {info_api.get('lat', 'Inconnu')}")
        print(f"Longitude : {info_api.get('lon', 'Inconnu')}")
        print(f"Organisation : {info_api.get('org', 'Inconnu')}")
        print(f"ASN : {info_api.get('as', 'Inconnu')}")
        print(f"Fournisseur : {info_api.get('isp', 'Inconnu')}")
        print(f"Mobile : {'Oui' if info_api.get('mobile', False) else 'Non'}")
        print(f"Proxy : {'Oui' if info_api.get('proxy', False) else 'Non'}")
        print(f"Timezone : {info_api.get('timezone', 'Inconnu')}")
        
    if info_info:
        print(Fore.CYAN + f"\nInformations de {ip} via web :")
        print(Fore.WHITE + f"Hostname : {info_info.get('hostname', 'Inconnu')}")
        print(f"Code pays : {info_info.get('country', 'Inconnu')}")
        print(f"Région : {info_info.get('region', 'Inconnu')}")
        print(f"Code postal : {info_info.get('postal', 'Inconnu')}")
        print(f"Organisation : {info_info.get('org', 'Inconnu')}")
        print(f"Localisation : {info_info.get('loc', 'Inconnu')}")
        print(f"Réseau : {info_info.get('network', 'Inconnu')}")
        print(f"Langue : {info_info.get('language', 'Inconnu')}")
    else:
        print(Fore.RED + "Impossible de récupérer les informations pour cette IP.")

get_ip_info2()

input(Fore.RED + "PRESS ENTER TO EXIT...")