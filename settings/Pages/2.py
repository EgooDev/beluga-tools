# Copyright (c) Beluga
# See the file 'LICENSE' for copying permission
# ----------------------------------------------------------------------------------------------------------------------------------------------------------|
# EN: 
#     - Do not touch or modify the code below. If there is an error, please contact the owner, but under no circumstances should you touch the code.
#     - Do not resell this tool, do not credit it to yours.
# FR: 
#     - Ne pas toucher ni modifier le code ci-dessous. En cas d'erreur, veuillez contacter le propriétaire, mais en aucun cas vous ne devez toucher au code.
#     - Ne revendez pas ce tool, ne le créditez pas au vôtre.

import os
import colorama
from pystyle import Center, Colorate, Colors, Anime
import subprocess
from colorama import Fore
import requests
import random

os.system("cls")
print(Colorate.Horizontal(Colors.blue_to_cyan,"""
┌─Github───────────────────┐┌─Others───────────────────┐┌─Discord 2/2──────────────┐     ___ ___ _   _   _  ___   _  
│                          ││                          ││                          │    | _ ) __| | | | | |/ __| /_\ 
│ [70]                     ││ [93] Mullvad Gen         ││ [116] Webhook Nuker      │    | _ \ _|| |_| |_| | (_ |/ _ \  
│ [71]                     ││ [94] Guns.lol Checker    ││ [117] Groupe Spammer     │    |___/___|____\___/ \___/_/ \_\ 
│ [72]                     ││ [95] Credit Card Checker ││ [118] Mass Report        │                                   
│ [73]                     ││ [96] Keylogger Maker     ││ [119] Server cloner      │        Author : Egoodev / xhe
│ [74]                     ││ [97] Netflix Checker     ││ [120] Token Multi-Tools  │     github.com/egoodev/Beluga-Tool 
│ [75]                     ││ [98] Tiktok Mass Report  ││                          │              Pages : 2/3
│ [76]                     ││ [99] Vbucks card Generate││                          │              
│ [77]                     ││ [100] Exe to Py          ││                          │  [N] Next  
│ [78]                     ││ [101] Azar Stealer       ││                          │  [B] Back
│ [79]                     ││ [102] Temp Mail          ││                          │  [I] Info
│ [80]                     ││ [103] CFX Lookup         ││                          │  [E] Exit
│ [81]                     ││ [104] Spotify Downloader ││                          │  
│ [82]                     ││ [105] Crypt URL Bypasser ││                          │  [H] Live Support
│ [83]                     ││ [106] CFX Scrapper       ││                          │    
│ [84]                     ││ [107]                    ││                          │  
│ [85]                     ││ [108]                    ││                          │   
│ [86]                     ││ [109]                    ││                          │  
│ [87]                     ││ [110]                    ││                          │   
│ [88]                     ││ [111]                    ││                          │  
│ [89]                     ││ [112]                    ││                          │  
│ [90]                     ││ [113]                    ││                          │  
│ [91]                     ││ [114]                    ││                          │  
│ [92]                     ││ [115]                    ││                          │  
└──────────────────────────┘└──────────────────────────┘└──────────────────────────┘    
                          
"""))
choice = input(Fore.BLUE + "Beluga@Admin/" + Fore.CYAN + "Root>" + Fore.WHITE)

while True:
#==================System==================
    if choice =='E':
        os.system(exit)
    if choice =='e':
        os.system(exit)

    elif choice in ['N', 'n']:
        os.system('cls')
        script_path = os.path.join('settings', 'Pages', 'OT.py')
        if os.path.isfile(script_path):
            subprocess.run(['python', script_path])

    elif choice in ['h', 'H']:
        os.system('cls')
        script_path = os.path.join('settings', 'Support', 'Support.py')
        if os.path.isfile(script_path):
            subprocess.run(['python', script_path])

    if choice =='i':
        os.system('cls')
        script_path = os.path.join('settings', 'About.py')
        if os.path.isfile(script_path):
            subprocess.run(['python', script_path])

    if choice =='I':
        os.system('cls')
        script_path = os.path.join('settings', 'About.py')
        if os.path.isfile(script_path):
            subprocess.run(['python', script_path])

    if choice =='b':
        os.system('cls')
        script_path = os.path.join('main.py')
        if os.path.isfile(script_path):
            subprocess.run(['python', script_path])

    if choice =='B':
        os.system('cls')
        script_path = os.path.join('main.py')
        if os.path.isfile(script_path):
            subprocess.run(['python', script_path])

    #==================System==================


    if choice =='93':
        os.system('cls')
        script_path = os.path.join('settings', 'Generator', 'Mullvad.py')
        if os.path.isfile(script_path):
            subprocess.run(['python', script_path])
        
    if choice =='94':
        os.system('cls')
        script_path = os.path.join('settings', 'others', 'guns.lol.py')
        if os.path.isfile(script_path):
            subprocess.run(['python', script_path])

    if choice =='95':
        os.system('cls')
        script_path = os.path.join('settings', 'others', 'CC Checker.py')
        if os.path.isfile(script_path):
            subprocess.run(['python', script_path])


    if choice =='96':
        os.system('cls')
        script_path = os.path.join('settings', 'others', 'KeyLogger Maker.py')
        if os.path.isfile(script_path):
            subprocess.run(['python', script_path])

    if choice =='97':
        os.system('cls')
        script_path = os.path.join('settings', 'others', 'Netflix Checker.py')
        if os.path.isfile(script_path):
            subprocess.run(['python', script_path])

    if choice =='98':
        os.system('cls')
        script_path = os.path.join('settings', 'others', 'Tiktok Mass Report.py')
        if os.path.isfile(script_path):
            subprocess.run(['python', script_path])

    if choice =='99':
        os.system('cls')
        script_path = os.path.join('settings', 'Generator', 'Vbucks.py')
        if os.path.isfile(script_path):
            subprocess.run(['python', script_path])

    if choice =='100':
        os.system('cls')
        script_path = os.path.join('settings', 'others', 'Exe to Py.py')
        if os.path.isfile(script_path):
            subprocess.run(['python', script_path])

    if choice =='101':
        os.system('cls')
        script_path = os.path.join('settings', 'others', 'AzarNuker.py')
        if os.path.isfile(script_path):
            subprocess.run(['python', script_path])

    if choice =='102':
        os.system('cls')
        script_path = os.path.join('settings', 'others', 'TempMail.py')
        if os.path.isfile(script_path):
            subprocess.run(['python', script_path])

    if choice =='103':
        os.system('cls')
        script_path = os.path.join('settings', 'others', 'CFX Lookup.py')
        if os.path.isfile(script_path):
            subprocess.run(['python', script_path])

    if choice =='104':
        os.system('cls')
        script_path = os.path.join('settings', 'others', 'Spotify downloader.py')
        if os.path.isfile(script_path):
            subprocess.run(['python', script_path])

    if choice =='105':
        os.system('cls')
        script_path = os.path.join('settings', 'others', 'Bypass URL.py')
        if os.path.isfile(script_path):
            subprocess.run(['python', script_path])

    if choice =='106':
        os.system('cls')
        script_path = os.path.join('settings', 'others', 'CFX Scrapper.py')
        if os.path.isfile(script_path):
            subprocess.run(['python', script_path])

    #=================Other=================



    #=================Other=================

    if choice =='116':
        os.system('cls')
        script_path = os.path.join('settings', 'others', 'Grab deleter.py')
        if os.path.isfile(script_path):
            subprocess.run(['python', script_path])

    if choice =='117':
        os.system('cls')
        script_path = os.path.join('settings', 'Discord', 'Groupe Spam.py')
        if os.path.isfile(script_path):
            subprocess.run(['python', script_path])

    if choice =='118':
        os.system('cls')
        script_path = os.path.join('settings', 'Discord', 'Mass Report.py')
        if os.path.isfile(script_path):
            subprocess.run(['python', script_path])

    if choice =='119':
        os.system('cls')
        script_path = os.path.join('settings', 'Discord', 'Server cloner.py')
        if os.path.isfile(script_path):
            subprocess.run(['python', script_path])

    if choice =='120':
        os.system('cls')
        script_path = os.path.join('settings', 'Raider', 'Raider.py')
        if os.path.isfile(script_path):
            subprocess.run(['python', script_path])





