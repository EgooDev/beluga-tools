import re
import sys
from urllib.parse import quote_plus
import requests
import json
from pystyle import Center, Colorate, Colors, Anime
from colorama import Fore
import os
from colorama import Fore

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
APIURL = "https://api.xposedornot.com/v1/breach-analytics?email="

EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

def get_email_from_user(prompt="Enter Email to check: "):
    email = input(prompt).strip()
    if not EMAIL_RE.match(email):
        print("Invalid mail.", file=sys.stderr)
        return None
    return email

def call_api(email, timeout=10):
    encoded = quote_plus(email)
    url = APIURL + encoded
    try:
        resp = requests.get(url, timeout=timeout)
    except requests.RequestException as e:
        print(f"Error API", file=sys.stderr)
        return None, None
    if resp.status_code != 200:
        print(f"API Status {resp.status_code} : {resp.text}", file=sys.stderr)
        return None, resp
    try:
        data = resp.json()
    except ValueError:
        print("Json Invalid.", file=sys.stderr)
        return None, resp
    return data, resp

def pretty_print_json(data):
    print(json.dumps(data, ensure_ascii=False, indent=2))

def main():
    email = get_email_from_user()
    if not email:
        return

    data, resp = call_api(email)
    if data is None:
        return

    print("JSON response :")
    pretty_print_json(data)
    if isinstance(data, dict):
        if "breaches" in data:
            breaches = data["breaches"]
            print(f"- Number of breaches found : {len(breaches)}")
            for i, b in enumerate(breaches, 1):
                name = b.get("name", "<nom inconnu>")
                date = b.get("date", b.get("breachDate", "date inconnue"))
                print(f"  {i}. {name} ({date})")
        else:
            # affiche quelques clés top-level
            for k in ("email", "pwned", "summary"):
                if k in data:
                    print(f"- {k} : {data[k]}")
    else:
        print("The response is not a JSON dictionary (type:", type(data), ")")

main()
input(Fore.RED + "Press Enter to exit...")
