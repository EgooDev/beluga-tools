from pystyle import Center, Colorate, Colors, Anime
from colorama import Fore
import os
import subprocess
import discord

def check_discord_version(expected_version="1.7.1"):
    current_version = discord.__version__
    if current_version == expected_version:
        print(f"✅ discord.py est bien en version {expected_version}")
    else:
        os.system("pip uninstall -y discord.py")
        os.system(f"pip install discord.py=={expected_version}")

check_discord_version()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    clear_screen()
    os.system('pip show discord.py')
    print(Colorate.Vertical(Colors.green_to_cyan, "installing dependencies..."))
    clear_screen()
    print(Colorate.Vertical(Colors.yellow_to_red, """
                                                                    
                                       (       (                   )\ )         (     
                                       ( )\    ( )\  (  (  (     )  (()/(   ) (   )\ )  
                                      )((_)  ))((_)))\ )\))( ( /(   /(_)| /( )\ (()/(  
                                     ((_)_  /((_) /((_|(_))\ )(_)) (_)) )(_)|(_) ((_)) 
                                      | _ )(_))| (_))( (()(_|(_)_  | _ ((_)_ (_) _| |  
                                      | _ \/ -_) | || / _` |/ _` | |   / _` || / _` |  
                                      |___/\___|_|\_,_\__, |\__,_| |_|_\__,_||_\__,_|  
                                                      |___/     

                                                 ┏━━━━━━━━━━━━━━━━━━━━━┓
                                                 ┃  Author : Ego/xhe   ┃
                                                 ┃ Discord: .gg/xxxx   ┃
                                                 ┗━━━━━━━━━━━━━━━━━━━━━┛    

    ┌──────────────────────────┐┌──────────────────────────┐┌──────────────────────────┐┌──────────────────────────┐ 
    │ <01> Token Spammer       ││ <07> Mass Reactions      ││ <13> HypeSquads Changer  ││ <19> Statut Spammer      │   
    │ <02> Token Mass leaver   ││ <08> Vocal Tools         ││ <14> Guild Checker       ││ <20> Threads Spam        │ 
    │ <03> Token leaver        ││ <09> Onliner             ││ <15> Flood Spammer       ││ <21> Poll Spammer        │                                 
    │ <04> Token info          ││ <10> Statut changer      ││ <16> Logs Spammer        ││                          │      
    │ <05> Bio changer         ││ <11>                     ││ <17> Reactions Nuker     ││                          │   
    │ <06> Nickname changer    ││ <12> Token Checker       ││ <18> Silent Ping         ││                          │
    └──────────────────────────┘└──────────────────────────┘└──────────────────────────┘└──────────────────────────┘
                                                                                                    
"""))

def run_script(script_name):
    path = os.path.join('settings', 'Raider', 'sys', script_name)
    if os.path.isfile(path):
        subprocess.run(['python', path])
    else:
        print(Fore.RED + f"[!] Script not found: {script_name}")

while True:
    show_menu()
    choice = input(Colorate.Vertical(Colors.yellow_to_red, "beluga@menu$~Choice ~> "))

    if choice == '00':
        print("👋 Au revoir !")
        break

    scripts = {
        '1': 'Token Spammer.py',
        '2': 'Token Mass Leaver.py',
        '3': 'Token leavers.py',
        '4': 'Token info.py',
        '5': 'Bio changer.py',
        '6': 'Nickname changer.py',
        '7': 'Mass reaction.py',
        '8': 'Voice Tools.py',
        '9': 'Onlineacc.py',
        '10': 'Statut changer.py',
        '11': 'Statut changer.py',
        '12': 'Token Checker.py',
        '13': 'HypeSquads.py',
        '14': 'Guild Checker.py',
        '15': 'Flood Spamer.py',
        '16': 'Logs spam.py',
        '17': 'Reactions nuker.py',
        '18': 'Silent Ping.py',
        '19': 'Statut Spammer.py',
        '20': 'Threads Spam.py',
        '21': 'Poll Spammer.py'
    }

    if choice in scripts:
        clear_screen()
        run_script(scripts[choice])
        input(Fore.GREEN + "\nAppuie sur ENTRÉE pour retourner au menu...")
    else:
        print(Fore.RED + "❌ Choix invalide.")
        input("Appuie sur ENTRÉE pour réessayer...")
