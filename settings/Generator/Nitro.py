import random
import string
import json
import requests
import threading
from colorama import Fore, Style, init

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

init(autoreset=True)

def generate_nitro():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))

def check_nitro(code):
    url = f'https://discord.gift/{code}'
    response = requests.get(f'https://discordapp.com/api/v6/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true', timeout=1)
    return url, response.status_code == 200

def send_webhook(webhook_url, nitro_url):
    payload = {
        'embeds': [{
            'title': 'Nitro Valid!',
            'description': f"**Nitro:**\n```{nitro_url}```",
            'color': 16711680  
        }]
    }
    headers = {'Content-Type': 'application/json'}
    requests.post(webhook_url, data=json.dumps(payload), headers=headers)

def nitro_worker(webhook_url=None):
    nitro_code = generate_nitro()
    url, valid = check_nitro(nitro_code)
    
    if valid:
        print(f"{Fore.GREEN}[VALID] Nitro: {url}")
        if webhook_url:
            send_webhook(webhook_url, url)
    else:
        print(f"{Fore.RED}[INVALID] Nitro: {url}")

def start_generator(threads, webhook_url=None):
    while True:
        thread_list = [threading.Thread(target=nitro_worker, args=(webhook_url,)) for _ in range(threads)]
        for thread in thread_list:
            thread.start()
        for thread in thread_list:
            thread.join()

if __name__ == "__main__":
    webhook = input(f"{Fore.YELLOW}Use Webhook? (y/n): {Style.RESET_ALL}").strip().lower()
    webhook_url = input(f"{Fore.YELLOW}Enter Webhook URL: {Style.RESET_ALL}") if webhook in ['y', 'yes'] else None
    try:
        threads = int(input(f"{Fore.YELLOW}Number of Threads: {Style.RESET_ALL}"))
        start_generator(threads, webhook_url)
    except ValueError:
        print(f"{Fore.RED}Invalid number of threads.")
