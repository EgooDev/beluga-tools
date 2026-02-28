from pystyle import Center, Colorate, Colors, Anime
import colorama
import os
import requests
import json
import threading
import random
import string

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

def ErrorWebhook():
    print(colorama.Fore.RED + "Invalid Webhook URL.")
    exit()

def ErrorNumber():
    print(colorama.Fore.RED + "Invalid number of threads.")
    exit()

def generate_pseudo(length=16):
    characters = string.ascii_uppercase + string.digits
    pseudo = ''.join(random.choice(characters) for _ in range(length))
    return pseudo

def send_webhookrdm():
    headers = {
        'Content-Type': 'application/json'
    }
    username_webhook = generate_pseudo()
    avatar_webhook = "https://photosrush.com/wp-content/uploads/boy-discord-pfp-2.jpg"
    payload = {
        'content': message,
        'username': username_webhook,
        'avatar_url': avatar_webhook
    }
    try:
        response = requests.post(webhook_url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()
        print(colorama.Fore.GREEN + f"Message: {message} Status: Sent")
    except:
        print(colorama.Fore.RED + f"Message: {message} Status: Rate Limit")

def send_webhook():
    headers = {
        'Content-Type': 'application/json'
    }
    username_webhook = 'Beluga | By xhe'
    avatar_webhook = "https://photosrush.com/wp-content/uploads/boy-discord-pfp-2.jpg"
    payload = {
        'content': message,
        'username': username_webhook,
        'avatar_url': avatar_webhook
    }
    try:
        response = requests.post(webhook_url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()
        print(colorama.Fore.GREEN + f"Message: {message} Status: Sent")
    except:
        print(colorama.Fore.RED + f"Message: {message} Status: Rate Limit")

def requestrdm():
    threads = []
    try:
        for _ in range(int(threads_number)):
            t = threading.Thread(target=send_webhookrdm)
            t.start()
            threads.append(t)
    except:
        ErrorNumber()

    for thread in threads:
        thread.join()

def request():
    threads = []
    try:
        for _ in range(int(threads_number)):
            t = threading.Thread(target=send_webhook)
            t.start()
            threads.append(t)
    except:
        ErrorNumber()

    for thread in threads:
        thread.join()

try:
    webhook_url = input("Webhook URL -> ")
    randomname = input("Use random usernames? (y/n) -> ").lower()
    message = input("Message -> ")
    threads_number = int(input("Threads Number -> "))
    if randomname == 'y':
        while True:
            requestrdm()
    else:
        while True:
            request()

except Exception as e:
    print(colorama.Fore.RED + f"Error: {e}")
