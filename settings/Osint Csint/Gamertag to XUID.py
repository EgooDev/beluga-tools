from pystyle import Center, Colorate, Colors, Anime
from colorama import Fore
import os
import requests
import json
from datetime import datetime
import requests
import sys

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

def get_xuid_from_gamertag(api_key: str, gamertag: str):
    base = "https://xbl.io/api/v2"
    url = f"{base}/search/{requests.utils.requote_uri(gamertag)}"
    headers = {
        "X-Authorization": api_key,
        "Accept": "application/json"
    }

    try:
        resp = requests.get(url, headers=headers, timeout=10)
    except requests.RequestException as e:
        return None, f"Erreur réseau: {e}"

    if resp.status_code == 401:
        return None, "API key invalid (401)."
    if resp.status_code == 404:
        return None, "Gamertag not found (404)."
    if resp.status_code >= 400:
        return None, f"API Error {resp.status_code}: {resp.text}"

    try:
        data = resp.json()
    except ValueError:
        return None, "JSON Error."
    
    if isinstance(data, dict):
        if "profileUsers" in data and isinstance(data["profileUsers"], list) and data["profileUsers"]:
            first = data["profileUsers"][0]
            if "id" in first:
                return first["id"], None
        if "people" in data and isinstance(data["people"], list) and data["people"]:
            p = data["people"][0]
            if "xuid" in p:
                return p["xuid"], None
        if "xuid" in data:
            return data["xuid"], None
        if "id" in data:
            return data["id"], None

    if isinstance(data, list) and data:
        first = data[0]
        if isinstance(first, dict):
            for key in ("xuid", "id"):
                if key in first:
                    return first[key], None

    return None, Fore.RED + f"Unable to extract the XUID automatically. Raw response: {data}"

def main():
    api_key = input(Fore.BLUE + "Enter API Key (xbl.io): " + Fore.WHITE)
    if not api_key:
        print("API Key required. Exiting.")
        sys.exit(1)

    gamertag = input(Fore.BLUE + "Enter Gamertags: " + Fore.WHITE)
    if not gamertag:
        print("Gamertag required. Exiting.")
        sys.exit(1)

    xuid, err = get_xuid_from_gamertag(api_key, gamertag)
    if err:
        print("Error :", err)
        sys.exit(1)

    print(Fore.BLUE + "Gamertag:" + Fore.WHITE + f" {gamertag}" + Fore.BLUE + "\nXUID:" + Fore.WHITE + f"{xuid}")

main()
