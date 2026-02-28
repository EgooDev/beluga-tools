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

HUDSONROCK_API_URL = "https://cavalier.hudsonrock.com/api/json/v2/osint-tools/search-by-email"
HUDSONROCK_API_KEY = os.getenv("HUDSONROCK_API_KEY", "ROCKHUDSONROCK")

def search_email(email):
    headers = {
        "x-api-key": HUDSONROCK_API_KEY,
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0"
    }

    params = {"email": email}

    try:
        response = requests.get(HUDSONROCK_API_URL, headers=headers, params=params, timeout=15)

        if response.status_code == 200:
            data = response.json()
            stealers = data.get("stealers") or []
            
            if not stealers:
                print(f"Aucun log stealer trouvé pour : {email}")
                return
            
            s = stealers[0]

            print("Compromission trouvée :\n")
            print(f"Ordinateur: {s.get('computer_name', 'N/A')}")
            print(f"Date: {s.get('date_compromised', 'N/A')}")
            print(f"OS: {s.get('operating_system', 'N/A')}")
            print(f"IP: {s.get('ip', 'N/A')}")
            print(f"Antivirus: {', '.join(s.get('antiviruses', [])) or 'Aucun'}")
            print(f"Top logins: {', '.join(s.get('top_logins', [])) or 'Aucun'}")

        elif response.status_code in (401, 403):
            print("Invalid API Key.")
        elif response.status_code == 404:
            print("Endpoint not found.")
        else:
            print(f"Error HTTP {response.status_code}: {response.text}")

    except requests.exceptions.Timeout:
        print("Timeout API.")
    except requests.exceptions.RequestException as e:
        print(f"Error {e}")



email = input(Fore.BLUE + "Entrez un email à vérifier : " + Fore.WHITE).strip()
search_email(email)
input(Fore.RED + "Appuyez sur Entrée pour revenir en arrière...")

