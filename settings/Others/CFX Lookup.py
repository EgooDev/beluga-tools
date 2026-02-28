import sys
from pystyle import Center, Colorate, Colors, Anime
from colorama import Fore
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


cfx_code = input(Colorate.Horizontal(Colors.blue_to_cyan, "Enter the CFX code: "))
def lookupcfx(cfx_code):

    server_id = cfx_code[-6:]


    api_url = f"https://servers-frontend.fivem.net/api/servers/single/{server_id}"

    headers = {
        'User-Agent': 'YourAppName/1.0',
        'Accept': 'application/json',
    }

    try:

        response = requests.get(api_url, headers=headers)


        if response.status_code == 200:

            data = response.json()


            data_content = data.get('Data', {})
            print("tu peux lookup ip pour voir il est chez quel isp si c'est un lien utilise nslookup sur le web </>")
            info = {
                'ownerID': data_content.get('ownerID'),
                'private': data_content.get('private'),
                'fallback': data_content.get('fallback'),
                'connectEndPoints': data_content.get('connectEndPoints'),
                'upvotePower': data_content.get('upvotePower'),
                'burstPower': data_content.get('burstPower'),
                'support_status': data_content.get('support_status'),
                'svMaxclients': data_content.get('svMaxclients'),
                'ownerName': data_content.get('ownerName'),
                'ownerProfile': data_content.get('ownerProfile'),
                'ownerAvatar': data_content.get('ownerAvatar'),
                'lastSeen': data_content.get('lastSeen'),
                'iconVersion': data_content.get('iconVersion')
            }


            for key, value in info.items():
                print(f"{key}: {value}")

        else:
            print(f"Erreur HTTP {response.status_code}: {response.reason}")

    except requests.RequestException as e:
        print(f"Erreur lors de la récupération des données: {e}")

lookupcfx(cfx_code)
input(Colorate.Horizontal(Colors.blue_to_cyan, "Press Enter to continue..."))