import requests
import threading
import os
from pystyle import Center, Colorate, Colors, Anime
from colorama import Fore, Style

os.system('cls')

print(Colorate.Horizontal(Colors.blue_to_cyan, """
 /$$$$$$$  /$$$$$$$$ /$$       /$$   /$$  /$$$$$$   /$$$$$$ 
| $$__  $$| $$_____/| $$      | $$  | $$ /$$__  $$ /$$__  $$ 
| $$  \ $$| $$      | $$      | $$  | $$| $$  \__/| $$  \ $$ 
| $$$$$$$ | $$$$$   | $$      | $$  | $$| $$ /$$$$| $$$$$$$$ 
| $$__  $$| $$__/   | $$      | $$  | $$| $$|_  $$| $$__  $$ 
| $$  \ $$| $$      | $$      | $$  | $$| $$  \ $$| $$  \ $$ 
| $$$$$$$/| $$$$$$$$| $$$$$$$$|  $$$$$$/|  $$$$$$/| $$  | $$ 
|_______/ |________/|________/ \______/  \______/ |__/  |__/ 

                ┏━━━━━━━━━━━━━━━━━━━━━┓
                ┃  Author : Ego/xhe   ┃
                ┃ Discord: .gg/xxxx   ┃
                ┗━━━━━━━━━━━━━━━━━━━━━┛
                          
"""))

def get_token_info(token):
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    r = requests.get('https://discord.com/api/v8/users/@me', headers=headers)
    if r.status_code != 200:
        print(f"{Fore.RED}[ERROR] Invalid token.")
        exit()
    return headers

def delete_dm(token, channels):
    headers = {'Authorization': token}
    for channel in channels:
        try:
            requests.delete(f'https://discord.com/api/v7/channels/{channel["id"]}', headers=headers)
            print(f"{Fore.GREEN}[DELETED] Channel: {channel['id']}")
        except Exception as e:
            print(f"{Fore.RED}[ERROR] Could not delete channel {channel['id']} - {e}")

def main():
    token = input(f"{Fore.YELLOW}Enter Discord Token: {Style.RESET_ALL}").strip()
    headers = get_token_info(token)

    channels = requests.get("https://discord.com/api/v9/users/@me/channels", headers=headers).json()
    if not channels:
        print(f"{Fore.BLUE}[INFO] No DM channels found.")
        return

    threads = []
    for chunk in [channels[i:i+3] for i in range(0, len(channels), 3)]:
        t = threading.Thread(target=delete_dm, args=(token, chunk))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print(f"{Fore.YELLOW}[DONE] All DM channels deleted.")

if __name__ == "__main__":
    main()
