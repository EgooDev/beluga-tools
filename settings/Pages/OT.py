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

print(Colorate.Horizontal(Colors.blue_to_cyan,"""
┌─github.com/dawa4real─────┐┌──────────────────────────┐┌──────────────────────────┐    ___ ___ _   _   _  ___   _  
│                          ││                          ││                          │   | _ ) __| | | | | |/ __| /_\ 
│ [1] Dox Create           ││                          ││                          │   | _ \ _|| |_| |_| | (_ |/ _ \  
│ [2] EMAIL BOMBER         ││                          ││                          │   |___/___|____\___/ \___/_/ \_\   
│ [3] email info           ││                          ││                          │                                 
│ [4] email spam reset     ││                          ││                          │        Author : Egoodev / xhe
│ [5] Dawa Gen             ││                          ││                          │    github.com/egoodev/Beluga-Tool
│ [6] Ip Lookup            ││                          ││                          │             Pages : 3/3
│ [7] IP Gen               ││                          ││                          │    
│ [8] IP Localisation      ││                          ││                          │  [N] Next
│ [9] IP Lookup            ││                          ││                          │  [B] Back
│ [10] Open Port           ││                          ││                          │  [I] Info
│ [11] IP Operator         ││                          ││                          │  [E] Exit
│ [12] IP Pinger           ││                          ││                          │    
│ [13] Name Finder         ││                          ││                          │  [H] Live Support
│ [14] Nitro Gen           ││                          ││                          │  
│ [15] Search Data Base    ││                          ││                          │  
│ [16] Simple Dox          ││                          ││                          │  
│ [17] INSTALL DAWA TOOLS  ││                          ││                          │  
│                          ││                          ││                          │  
│                          ││                          ││                          │   
│                          ││                          ││                          │  
│                          ││                          ││                          │  
│                          ││                          ││                          │   
│                          ││                          ││                          │  
└──────────────────────────┘└──────────────────────────┘└──────────────────────────┘                         
"""))
choice = input(Fore.BLUE + "Beluga@Admin/" + Fore.CYAN + "Root>" + Fore.WHITE)

while True:
#==================System==================
    if choice =='E':
        os.system(exit)
    if choice =='e':
        os.system(exit)

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
        script_path = os.path.join('settings','Pages','2.py')
        if os.path.isfile(script_path):
            subprocess.run(['python', script_path])

    if choice =='B':
        os.system('cls')
        script_path = os.path.join('settings','Pages','2.py')
        if os.path.isfile(script_path):
            subprocess.run(['python', script_path])

    #==================System==================

    if choice =='1':
        os.system('cls')
        script_path = os.path.join('settings', 'OthersTools', 'dawa4real', 'dawa_dox_fr.py')
        if os.path.isfile(script_path):
            subprocess.run(['python', script_path])

    if choice =='2':
        os.system('cls')
        script_path = os.path.join('settings', 'OthersTools', 'dawa4real', 'dawa_Email_bomber_fr.py')
        if os.path.isfile(script_path):
            subprocess.run(['python', script_path])

    if choice =='3':
        os.system('cls')
        script_path = os.path.join('settings', 'OthersTools', 'dawa4real', 'dawa_Email_info_fr.py')
        if os.path.isfile(script_path):
            subprocess.run(['python', script_path])

    if choice =='4':
        os.system('cls')
        script_path = os.path.join('settings', 'OthersTools', 'dawa4real', 'dawa_Email_spam_reset_fr.py')
        if os.path.isfile(script_path):
            subprocess.run(['python', script_path])

    if choice =='5':
        os.system('cls')
        script_path = os.path.join('settings', 'OthersTools', 'dawa4real', 'dawa_gen_fr.py')
        if os.path.isfile(script_path):
            subprocess.run(['python', script_path])

    if choice =='6':
        os.system('cls')
        script_path = os.path.join('settings', 'OthersTools', 'dawa4real', 'dawa_IP_all_lookup_fr.py')
        if os.path.isfile(script_path):
            subprocess.run(['python', script_path])

    if choice =='7':
        os.system('cls')
        script_path = os.path.join('settings', 'OthersTools', 'dawa4real', 'dawa_IP_gen_fr.py')
        if os.path.isfile(script_path):
            subprocess.run(['python', script_path])

    if choice =='8':
        os.system('cls')
        script_path = os.path.join('settings', 'OthersTools', 'dawa4real', 'dawa_IP_localisation_fr.py')
        if os.path.isfile(script_path):
            subprocess.run(['python', script_path])

    if choice =='9':
        os.system('cls')
        script_path = os.path.join('settings', 'OthersTools', 'dawa4real', 'dawa_Ip_lookup_fr.py')
        if os.path.isfile(script_path):
            subprocess.run(['python', script_path])

    if choice =='10':
        os.system('cls')
        script_path = os.path.join('settings', 'OthersTools', 'dawa4real', 'dawa_IP_openport_fr.py')
        if os.path.isfile(script_path):
            subprocess.run(['python', script_path])

    if choice =='11':
        os.system('cls')
        script_path = os.path.join('settings', 'OthersTools', 'dawa4real', 'dawa_IP_operator_fr.py')
        if os.path.isfile(script_path):
            subprocess.run(['python', script_path])

    if choice =='12':
        os.system('cls')
        script_path = os.path.join('settings', 'OthersTools', 'dawa4real', 'dawa_IP_pinger_fr.py')
        if os.path.isfile(script_path):
            subprocess.run(['python', script_path])

    if choice =='13':
        os.system('cls')
        script_path = os.path.join('settings', 'OthersTools', 'dawa4real', 'dawa_Name_finder_fr.py')
        if os.path.isfile(script_path):
            subprocess.run(['python', script_path])

    if choice =='14':
        os.system('cls')
        script_path = os.path.join('settings', 'OthersTools', 'dawa4real', 'dawa_Nitro_gen_fr.py')
        if os.path.isfile(script_path):
            subprocess.run(['python', script_path])

    if choice =='15':
        os.system('cls')
        script_path = os.path.join('settings', 'OthersTools', 'dawa4real', 'dawa_Searsh_data_base_fr.py')
        if os.path.isfile(script_path):
            subprocess.run(['python', script_path])

    if choice =='16':
        os.system('cls')
        script_path = os.path.join('settings', 'OthersTools', 'dawa4real', 'dawa_simple_dox_fr.py')
        if os.path.isfile(script_path):
            subprocess.run(['python', script_path])

    if choice =='17':
        os.system('cls')
        script_path = os.path.join('settings', 'OthersTools', 'dawa4real', 'install.py')
        if os.path.isfile(script_path):
            subprocess.run(['python', script_path])

