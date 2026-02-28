import requests
import json
import os
import time
import re
import uuid
from fake_useragent import UserAgent
from colorama import init, Fore, Style
import phonenumbers
from phonenumbers import geocoder, carrier
import math
import socket
import colorama
from colorama import Fore
import os
import subprocess
import time
import webbrowser
import threading
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

init()

DUMP_DIR = 'Output/FiveM Scap'
SERVER_FILE = 'input/server.txt'
PROXY_FILE = 'input/proxy.txt'
SLEEP_TIME = 1

def clean_filename(hostname):
    return re.sub(r'[<>:"/\\|?*]', '', hostname)

def check_if_player_exists(filename, player_data, added_players):
    if not os.path.exists(filename):
        return False

    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        try:
            existing_player = json.loads(line)
        except json.JSONDecodeError:
            continue

        if existing_player.get('fivem') == player_data.get('fivem'):
            fields_to_check = ['steam', 'name', 'live', 'xbl', 'license', 'license2', 'name']
            if all(existing_player.get(field) == player_data.get(field) for field in fields_to_check):
                return True

    return player_data['identifiers'] in added_players

def get_server_information(server_id, proxy, added_players):
    url = f'https://servers-frontend.fivem.net/api/servers/single/{server_id}'
    headers = {'User-Agent': UserAgent().random}

    try:
        response = requests.get(url, headers=headers, proxies=proxy)

        if response.status_code == 200:
            server_data = response.json()
            hostname = clean_filename(server_data.get('Data', {}).get('hostname', str(uuid.uuid4())))[:100]

            project_name = server_data.get('Data', {}).get('vars', {}).get('sv_projectName', '')
            if len(project_name) >= 10:
                hostname = clean_filename(project_name)[:100]

            os.makedirs(DUMP_DIR, exist_ok=True)
            filename = f'{DUMP_DIR}/{hostname}.txt'
            players_added_count = 0

            for player in server_data['Data'].get('players', []):
                player_data = json.dumps(player, ensure_ascii=False)
                if not check_if_player_exists(filename, player, added_players):
                    with open(filename, 'a', encoding='utf-8') as file:
                        file.write(player_data + '\n')

                    print(Fore.GREEN + f'[NOUVEAU] ' + Style.RESET_ALL + f'{player["name"]} a été ajouté !')
                    added_players.append(player['identifiers'])
                    players_added_count += 1

            print(Fore.CYAN + '[INFORMATION]' + Style.RESET_ALL + f' Nombre de joueurs ajoutés dans {filename}: {players_added_count}')
            print(Fore.CYAN + '[INFORMATION]' + Style.RESET_ALL + f' Nombre total de joueurs ajoutés : {len(added_players)}\n')

        else:
            print(Fore.RED + f'\n[ERREUR] Message d\'erreur, le serveur ({server_id}) na pas pus être trouver\n')

    except Exception as e:
        print(Fore.RED + f'Erreur: {str(e)}')

def process_servers(server_ids, proxies, added_players):
    for server_id, proxy in zip(server_ids, proxies):
        get_server_information(server_id, proxy, added_players)
        time.sleep(0.5)

def main():
    use_proxies = input("Voulez-vous utiliser des proxys ? (y/n) : ").strip().lower() == 'y'

    with open(SERVER_FILE, 'r') as server_file:
        server_ids = [line.strip() for line in server_file]

    proxy_list = []
    if use_proxies:
        with open(PROXY_FILE, 'r') as proxy_file:
            proxy_list = [{'http': f'socks5://{proxy.strip()}'} for proxy in proxy_file]

    added_players = []

    while True:
        half_length = len(server_ids) // 2
        first_half = server_ids[:half_length]
        second_half = server_ids[half_length:]

        if use_proxies:
            process_servers(first_half, proxy_list, added_players)
            process_servers(second_half, proxy_list, added_players)
        else:
            process_servers(first_half, [{} for _ in first_half], added_players)
            process_servers(second_half, [{} for _ in second_half], added_players)

        print(Fore.MAGENTA + f"\n[TIME] Attendez le prochain dump ({SLEEP_TIME}sec) ...\n")
        time.sleep(SLEEP_TIME)

def startup():
    time.sleep(1)
    main()


startup()