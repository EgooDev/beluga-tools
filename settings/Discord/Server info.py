import requests
from colorama import Fore, Style, init
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
init(autoreset=True)
def get_server_info(invite):
    invite_code = invite.split("/")[-1]
    response = requests.get(f"https://discord.com/api/v9/invites/{invite_code}")

    if response.status_code != 200:
        print(f"{Fore.RED}[ERROR] Invalid invitation link.")
        return

    api = response.json()
    server_info = api.get('guild', {})
    inviter_info = api.get('inviter', {})

    print(f"""{Fore.YELLOW}
    ─── Discord Server Information ───
    {Fore.CYAN}Invitation        : {Fore.WHITE}{invite}
    {Fore.CYAN}Type              : {Fore.WHITE}{api.get('type', 'None')}
    {Fore.CYAN}Code              : {Fore.WHITE}{api.get('code', 'None')}
    {Fore.CYAN}Expires At        : {Fore.WHITE}{api.get('expires_at', 'None')}
    {Fore.CYAN}Server ID         : {Fore.WHITE}{server_info.get('id', 'None')}
    {Fore.CYAN}Server Name       : {Fore.WHITE}{server_info.get('name', 'None')}
    {Fore.CYAN}Description       : {Fore.WHITE}{server_info.get('description', 'None')}
    {Fore.CYAN}NSFW Level        : {Fore.WHITE}{server_info.get('nsfw_level', 'None')}
    {Fore.CYAN}Verification Lv.  : {Fore.WHITE}{server_info.get('verification_level', 'None')}
    {Fore.CYAN}Boosts            : {Fore.WHITE}{server_info.get('premium_subscription_count', 'None')}
    """)

    if inviter_info:
        print(f"""{Fore.MAGENTA}
    ─── Inviter Information ───
    {Fore.CYAN}ID               : {Fore.WHITE}{inviter_info.get('id', 'None')}
    {Fore.CYAN}Username         : {Fore.WHITE}{inviter_info.get('username', 'None')}
    {Fore.CYAN}Global Name      : {Fore.WHITE}{inviter_info.get('global_name', 'None')}
    {Fore.CYAN}Avatar           : {Fore.WHITE}{inviter_info.get('avatar', 'None')}
    {Fore.CYAN}Banner           : {Fore.WHITE}{inviter_info.get('banner', 'None')}
    """)

if __name__ == "__main__":
    invite = input(f"{Fore.YELLOW}Enter Server Invitation: {Style.RESET_ALL}").strip()
    get_server_info(invite)
    input("Press enter to back menu..")