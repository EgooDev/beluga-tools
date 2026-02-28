from pystyle import Center, Colorate, Colors, Anime
import colorama
import os
import requests

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
    print(colorama.Fore.BLUE + "Invalid Webhook URL.")
    exit()

def info_webhook(webhook_url):
    headers = {
        'Content-Type': 'application/json',
    }

    response = requests.get(webhook_url, headers=headers)
    webhook_info = response.json()

    webhook_id = webhook_info.get('id', "None")
    webhook_token = webhook_info.get('token', "None")
    webhook_name = webhook_info.get('name', "None")
    webhook_avatar = webhook_info.get('avatar', "None")
    webhook_type = "bot" if webhook_info.get('type') == 1 else "webhook utilisateur"
    channel_id = webhook_info.get('channel_id', "None")
    guild_id = webhook_info.get('guild_id', "None")

    print(f"""
    ID         : {colorama.Fore.WHITE}{webhook_id}{colorama.Fore.BLUE}
    Token      : {colorama.Fore.WHITE}{webhook_token}{colorama.Fore.BLUE}
    Name       : {colorama.Fore.WHITE}{webhook_name}{colorama.Fore.BLUE}
    Avatar     : {colorama.Fore.WHITE}{webhook_avatar}{colorama.Fore.BLUE}
    Type       : {colorama.Fore.WHITE}{webhook_type}{colorama.Fore.BLUE}
    Channel ID : {colorama.Fore.WHITE}{channel_id}{colorama.Fore.BLUE}
    Server ID  : {colorama.Fore.WHITE}{guild_id}{colorama.Fore.BLUE}
    """)

    if 'user' in webhook_info:
        user_info = webhook_info['user']
        
        user_id = user_info.get('id', "None")
        username = user_info.get('username', "None")
        display_name = user_info.get('global_name', "None")
        discriminator = user_info.get('discriminator', "None")
        user_avatar = user_info.get('avatar', "None")
        user_flags = user_info.get('flags', "None")
        accent_color = user_info.get('accent_color', "None")
        avatar_decoration = user_info.get('avatar_decoration_data', "None")
        banner_color = user_info.get('banner_color', "None")

        print(f"""
    User information associated with the Webhook:
    ID          : {colorama.Fore.WHITE}{user_id}{colorama.Fore.BLUE}
    Name        : {colorama.Fore.WHITE}{username}{colorama.Fore.BLUE}
    DisplayName : {colorama.Fore.WHITE}{display_name}{colorama.Fore.BLUE}
    Number      : {colorama.Fore.WHITE}{discriminator}{colorama.Fore.BLUE}
    Avatar      : {colorama.Fore.WHITE}{user_avatar}{colorama.Fore.BLUE}
    Flags       : {colorama.Fore.WHITE}{user_flags} Publique: {user_flags}{colorama.Fore.BLUE}
    Color       : {colorama.Fore.WHITE}{accent_color}{colorama.Fore.BLUE}
    Decoration  : {colorama.Fore.WHITE}{avatar_decoration}{colorama.Fore.BLUE}
    Banner      : {colorama.Fore.WHITE}{banner_color}{colorama.Fore.BLUE}
    """)

def CheckWebhook(webhook_url):
    try:
        response = requests.get(webhook_url)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False

webhook_url = input(f"{colorama.Fore.WHITE}Enter Webhook URL -> {colorama.Fore.RESET}")
if not CheckWebhook(webhook_url):
    ErrorWebhook()
info_webhook(webhook_url)
input(" ")
