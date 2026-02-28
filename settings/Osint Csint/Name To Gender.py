import requests
from pystyle import Center, Colorate, Colors, Anime
from colorama import Fore
import os
import subprocess

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
name  = input(Fore.BLUE + "Enter Name: ")
res = requests.get(f'https://api.genderize.io/?name={name}')
data = res.json()
gender = data.get('gender','N/A')
propability = data.get('probability','N/A')
nome = data.get('name','N/A')
count = data.get('count','N/A')
print()
print(Fore.CYAN + f"""
Name : {nome}
Gender : {gender}
Propability : {propability}%
Count : {count}""")
print()
input("Press enter to go back...")