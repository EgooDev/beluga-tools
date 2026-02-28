import websocket
import json
import os
import time
import requests
from pystyle import Center, Colorate, Colors, Anime
from colorama import Fore
import os
import subprocess
import requests
import random
import os
import discord

os.system('cls')
print(Colorate.Vertical(Colors.yellow_to_red,"""
                                                                    
                    (       (                   )\ )         (     
                     ( )\    ( )\  (  (  (     )  (()/(   ) (   )\ )  
                    )((_)  ))((_)))\ )\))( ( /(   /(_)| /( )\ (()/(  
                   ((_)_  /((_) /((_|(_))\ )(_)) (_)) )(_)|(_) ((_)) 
                    | _ )(_))| (_))( (()(_|(_)_  | _ ((_)_ (_) _| |  
                    | _ \/ -_) | || / _` |/ _` | |   / _` || / _` |  
                    |___/\___|_|\_,_\__, |\__,_| |_|_\__,_||_\__,_|  
                                     |___/     
                      
"""))

def tokens():
    token_path = "input/tokens.txt"
    
    if not os.path.exists(token_path):
        print("[❌] The 'tokens.txt' file is missing.")
        return []

    with open(token_path, "r") as file:
        return [line.strip() for line in file if line.strip()]

def print_success(token):
    print(f"[✅] Reaction sent successfully")

def print_err(token, response):
    print(f"[❌] Failed to send reaction")
    print(f"[🔴] Status Code: {response.status_code}")
    print(f"[🔴] Response Body: {response.text}")

def print_logo():
    print("Your logo here")

def print_(message):
    print(message)

def random_useragent():
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
    ]
    return random.choice(user_agents)

async def send_reaction():
    print_logo()
    print_('[=] Enter the channel id:')
    chid = input().strip()
    
    print_('[=] Enter the message id:')
    msgid = input().strip()

    print_('[=] Enter the emoji (Normal Emojis or "ID" for custom emojis):')
    emoji_ = input().strip()

    emoji = f'sex:{emoji_}' if emoji_.isalnum() else str(emoji_)

    tks = tokens()

    if len(tks) > 0:
        print_logo()
        for token in tks:
            try:
                response = requests.put(
                    url=f'https://discord.com/api/v9/channels/{chid}/messages/{msgid}/reactions/{emoji}/@me',
                    headers={
                        "Authorization": token,
                        "User-Agent": random_useragent(),
                        "Content-Type": "application/json"
                    }
                )

                if response.status_code == 204:
                    print_success(token)
                else:
                    print_err(token, response)
            except requests.exceptions.RequestException as e:
                print(f"[❌] Request failed: {str(e)}")
                print_err(token, e)
        await tokenTools()  

    else:
        await tokenTools() 

async def tokenTools():
    print_("[=] No valid tokens found or operation completed.")

if __name__ == "__main__":
    import asyncio
    asyncio.run(send_reaction())