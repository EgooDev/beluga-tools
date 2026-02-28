import requests
from bs4 import BeautifulSoup
import colorama
from colorama import Fore
import os
import subprocess
import time
import webbrowser
from colorama import Fore, Style
from pystyle import Center, Colorate, Colors, Anime

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
def extraire_liens(url):
    try:

        response = requests.get(url)
        response.raise_for_status() 
        

        soup = BeautifulSoup(response.text, 'html.parser')
        

        liens = []
        for lien in soup.find_all('a', href=True):
            liens.append(lien['href'])
        
        return liens

    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"Erreur{e}")
        return []

def main():
    url = input(Fore.CYAN + "URL : " + Fore.MAGENTA)
    liens = extraire_liens(url)
    
    print(Fore.CYAN + "Grabber :")
    print(Fore.WHITE + " ")
    for lien in liens:
        print(lien)



if __name__ == "__main__":
    main()
    input(Fore.RED + "PRESS ENTER TO EXIT...")
