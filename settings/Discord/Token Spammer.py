from pystyle import Center, Colorate, Colors, Anime
import colorama
import os
import requests
import threading

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

def ErrorToken():
    print(colorama.Fore.RED + "Invalid Token.")
    exit()

def ErrorNumber():
    print(colorama.Fore.RED + "Invalid number of threads.")
    exit()

def spammer(token, channel, message):
    try:
        response = requests.post(
            f"https://discord.com/api/channels/{channel}/messages",
            data={'content': message},
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
                'Authorization': token
            }
        )
        response.raise_for_status()
        print(colorama.Fore.GREEN + f"Message: {message[:10]}... Channel: {channel} Status: Sent")
    except Exception as e:
        print(colorama.Fore.RED + f"Message: {message[:10]}... Channel: {channel} Status: Error {str(e)}")

def start_spamming():
    token = input("Enter your Discord token: ")
    channel = input("Enter the Channel ID: ")
    message = input("Enter the Spam Message: ")

    message_len = len(message)
    if message_len > 10:
        message_sensur = message[:10] + "..."
    else:
        message_sensur = message

    try:
        threads_number = int(input("Enter the number of threads (recommended: 2, 4): "))
    except:
        ErrorNumber()

    def request():
        threads = []
        try:
            for _ in range(threads_number):
                t = threading.Thread(target=spammer, args=(token, channel, message))
                t.start()
                threads.append(t)
        except:
            ErrorNumber()

        for thread in threads:
            thread.join()

    while True:
        request()

try:
    start_spamming()
except Exception as e:
    print(colorama.Fore.RED + f"Error: {e}")
