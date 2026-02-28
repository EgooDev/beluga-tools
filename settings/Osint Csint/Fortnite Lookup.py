from pystyle import Center, Colorate, Colors, Anime
from colorama import Fore
import os
from colorama import Fore
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
def fortnite_lookup_ultimate():
    API_KEY = input(Fore.BLUE + "Enter your Fortnite API Key (fortniteapi.io): " + Fore.WHITE).strip()
    username = input("\nEpic Username : ").strip()
    if not username:
        print("Enter Epic Username !")
        return

    headers = {"Authorization": API_KEY}
    print(f"\nLooking for {username}...")

    try:
        lookup = requests.get(f"https://fortniteapi.io/v1/lookup?username={username}", headers=headers, timeout=10)
        if lookup.status_code == 404:
            print(Fore.CYAN + "{username} not found.")
            return
        if lookup.status_code == 401:
            print("401, invalid key")
            return
        if lookup.status_code != 200:
            print(f"Error lookup : {lookup.status_code}")
            return

        account_id = lookup.json()["account_id"]
        print(f"ID Epic : {account_id}")

        stats = requests.get(f"https://fortniteapi.io/v1/stats?account={account_id}", headers=headers, timeout=15)
        stats_url = f"https://fortniteapi.io/v1/stats?account={account_id}&lang=fr"
        r2 = requests.get(stats_url, headers=headers, timeout=15)
        
        if r2.status_code != 200:
            print(Fore.RED + f"Erreur stats : {r2.status_code}")
            return        
        data = stats.json()
        acc = data.get("account", {})
        glob = data.get("global_stats", {})

        print(Colorate.Horizontal(Colors.blue_to_cyan, f" PLAYER : {data.get('name', username).upper()}"))
        print(Colorate.Horizontal(Colors.blue_to_cyan,  " EPIC ID : {account_id}"))
        print(Colorate.Horizontal(Colors.blue_to_cyan,  " LEVEL : {acc.get('level', 'N/A')} | BP : {acc.get('progress_pct', 0)}%"))
        print(Colorate.Horizontal(Colors.blue_to_cyan,  "*60"))

        modes = {
            "solo": "SOLO",
            "duo": "DUO", 
            "squad": "SQUAD",
            "reload": "RELOAD",
            "ranked_br": "RANKED BR",
            "ranked_zb": "RANKED ZB",
        }

        for key, name in modes.items():
            m = glob.get(key, {})
            if not m: 
                continue
            print(Colorate.Horizontal(Colors.blue_to_cyan, "\n{name}"))
            print(Fore.BLUE +                           f"  Victory       : {m.get('placetop1', 0):,}")
            print(Fore.BLUE +                           f"  Winrate       : {m.get('winrate', 0):.2f}%")
            print(Fore.BLUE +                           f"  K/D           : {m.get('kd', 0):.2f}")
            print(Fore.BLUE +                           f"  Kills         : {m.get('kills', 0):,}")
            print(Fore.BLUE +                           f"  Kills/match   : {m.get('kills_per_match', 0):.2f}")
            print(Fore.BLUE +                           f"  Games         : {m.get('matchesplayed', 0):,}")

        ranked = glob.get("ranked_br", {})
        if ranked:
            rank = ranked.get('rank', 'Unranked')
            div = ranked.get('division', '')
            print(Fore.BLUE + f"\n RANKED BR : {rank} {div}".strip())

        inputs = data.get("inputs", {})
        if inputs:
            print(Colorate.Horizontal(Colors.blue_to_cyan, + "\n INPUTS"))
            for inp, d in inputs.items():
                name = {"keyboardmouse": "Keyboard/Mouse", "gamepad": "Controller", "touch": "Mobile"}.get(inp, inp.title())
                print(Fore.BLUE + f"  {name} : {d.get('matchesplayed', 0):,} parties")

    except requests.exceptions.RequestException:
        print(Fore.RED + "Problem connecting to the API.")
    except Exception as e:
        print(Fore.RED + f"Error : {e}")

fortnite_lookup_ultimate()
input(Fore.RED + "Press enter to exit...")