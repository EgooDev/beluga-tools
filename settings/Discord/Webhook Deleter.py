from pystyle import Center, Colorate, Colors, Anime
import colorama
import requests
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

colorama.init(autoreset=True)

def ErrorWebhook():
    print(colorama.Fore.RED + "Error: Webhook could not be deleted.")
    exit()

def CheckWebhook(webhook_url):
    try:
        response = requests.head(webhook_url)
        return response.status_code == 200
    except:
        return False

def DeleteWebhook(webhook_url):
    try:
        response = requests.delete(webhook_url)
        response.raise_for_status()
        print(colorama.Fore.GREEN + "Webhook Deleted.")
    except:
        ErrorWebhook()

try:
    webhook_url = input(colorama.Fore.YELLOW + "URL Webhook -> ")
    
    if not CheckWebhook(webhook_url):
        ErrorWebhook()

    DeleteWebhook(webhook_url)
except Exception as e:
    print(colorama.Fore.RED + f"Error: {e}")
