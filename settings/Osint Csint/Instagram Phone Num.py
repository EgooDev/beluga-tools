import sys
import time
import json
import httpx
import hmac
import hashlib
import urllib.parse
import requests
from bs4 import BeautifulSoup
from colorama import Fore, init
import os
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

def get_user_id(username, session_id):
    try:
        url = f"https://www.instagram.com/{username}/?__a=1"
        headers = {"User-Agent": "Instagram 64.0.0.14.96"}
        cookies = {"sessionid": session_id}

        r = requests.get(url, headers=headers, cookies=cookies, timeout=10)
        data = json.loads(r.text)
        return data["logging_page_id"].replace("profilePage_", "")
    except:
        return None


def get_info(username, session_id):
    user_id = get_user_id(username, session_id)
    if not user_id:
        return None

    try:
        url = f"https://i.instagram.com/api/v1/users/{user_id}/info/"
        headers = {"User-Agent": "Instagram 64.0.0.14.96"}
        cookies = {"sessionid": session_id}

        r = requests.get(url, headers=headers, cookies=cookies, timeout=10)
        return r.json()["user"]
    except:
        return None


def advanced_lookup(username):
    URL = "https://i.instagram.com/api/v1/users/lookup/"
    SIG_KEY = "e6358aeede676184b9fe702b30f4fd35e71744605e39d2181a34cede076b3c33"

    def sign(data):
        sig = hmac.new(SIG_KEY.encode(), data.encode(), hashlib.sha256).hexdigest()
        return f"ig_sig_key_version=4&signed_body={sig}.{urllib.parse.quote_plus(data)}"

    payload = json.dumps({
        "login_attempt_count": "0",
        "directly_sign_in": "true",
        "source": "default",
        "q": username
    })

    try:
        headers = {"User-Agent": "Instagram 101.0.0.15.120"}
        r = httpx.post(URL, headers=headers, data=sign(payload))
        return r.json()
    except:
        return None


def search_accounts(name):
    url = "https://dumpor.com/search?query=" + name.replace(" ", "+")
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        r = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")

        accounts = []
        for a in soup.find_all("a", class_="profile-name-link"):
            accounts.append(a.text.replace("@", ""))

        return accounts
    except:
        return []


def main():
    session_id = input("Instagram SessionID: ")
    name = input("Full name: ")
    email = input("Target email: ")
    phone = input("Target phone: ")
    delay = input("Delay between requests (sec, optional): ")

    delay = int(delay) if delay else 0

    print("\nSearching for accounts...\n")
    accounts = search_accounts(name)

    if not accounts:
        print("No accounts found.")
        return

    for username in accounts:
        print(Fore.CYAN + f"\n===== {username} =====")

        info = get_info(username, session_id)
        if not info:
            print("Unable to retrieve info.")
            continue

        print("Name:", info.get("full_name"))
        print("Followers:", info.get("follower_count"))
        print("Private:", info.get("is_private"))
        print("Bio:", info.get("biography"))

        if info.get("public_email"):
            print(Fore.YELLOW + "Public email:", info["public_email"])

        if info.get("public_phone_number"):
            print(Fore.YELLOW + "Public phone:", info["public_phone_number"])

        adv = advanced_lookup(username)
        if adv and "obfuscated_email" in adv:
            print(Fore.GREEN + "Hidden email:", adv["obfuscated_email"])

        if delay:
            time.sleep(delay)

    print("\nFinished.")


main()
input("Press Enter to exit")