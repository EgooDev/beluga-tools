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
import time

os.system("cls")
print(Colorate.Horizontal(Colors.blue_to_cyan,"""
                                                    @@@@@@@@                           
                                                @@%+-.....:+%@@                        
                                              @@-..        ...#@@                      
                                            @@-..            ..+@                      
                                          @@#..               ..%@                     
                                       @@%+..                 ..#@@@@@                 
                                    @@#-.                    ..@=..:=%@@               
                                 @@%:..             .=#=.    ......:=@@                
                              @@%-..              .+@:  @-..:%=+#%@@@                  
                            @@*..                 .#@*@@@*..+@%#*#%@@@                 
                          @@*..                   ..+@@@=.......:-=-+@@                
                         @%..                       ...:===....--#@@@                  
                        @*..                        ..=====...:=@@                     
                      @@*..                         ...::....-+@@                      
                      @+..                          ... ....-*@                        
                     @#...              .:..        ......-=@@                         
                    @@-..             ..+=..    :.. ...--%@@@@                         
                    @+:.              .%*-..    =#---#%@*:...-@@                       
                   @@=:.             .*%-...    =@@@@#-:.... ..#@                      
                   @%-:             .=%-:.      +@   @@*-:.. .:@@                      
                   @%-:.            .@+-..    ..%@      @@@@@@@                        
                   @%-:..           -@--..   ..@@                                      
                    @+-:..         .*@#-:...:*%:#@@@%%@@@@                             
                    @@=-:...      .-+%%*#%#*=.:%#... ..-%@                             
                     @@=--:...    ....=%#-:..:@:.   ..:=@                              
                       @%----:..  ..   ...:-=-.   ..:-*@@                              
                     
"""))
time.sleep(1)
os.system('cls')
ascii = Colorate.Horizontal(Colors.blue_to_cyan,"""
┌──Discord 1/2─────────────┐┌─Osint / Csint────────────┐┌─Network / Web────────────┐    ___ ___ _   _   _  ___   _  
│                          ││                          ││                          │   | _ ) __| | | | | |/ __| /_\ 
│ [1] ID to Bot            ││ [24] Dox Template        ││ [47] IP Generator        │   | _ \ _|| |_| |_| | (_ |/ _ \  
│ [2] Nuke bot             ││ [25] Ez searcher         ││ [48] IP Lookup           │   |___/___|____\___/ \___/_/ \_\   
│ [3] Nitro Generator      ││ [26] Email Lookup        ││ [49] IP Pinger           │                                 
│ [4] Server info          ││ [27] Email Tracker       ││ [50] Port Scanner        │        Author : Egoodev / xhe
│ [5] Friends Block        ││ [28] Username Tracker    ││ [51] IP Scanner          │    github.com/egoodev/Beluga-Tool
│ [6] DM Deleter           ││ [29] Free intelX (No Pro)││ [52] Website Info Scan   │             Pages : 1/3
│ [7] Friends Deleter      ││ [30] Phone Lookup        ││ [53] Website Vuln Scan   │  
│ [8] Token Generator      ││ [31] Insta Profil Scrap  ││ [54] DoS (DDoS) Prox/sock│  [N] Next
│ [9] Hypesquad changer    ││ [32] Osint Beginer       ││ [55] Proxy Extractor     │  [B] Back
│ [10] Token info          ││ [33] IMG EXIF data       ││ [56] IP Grabber (.py)    │  [I] Info
│ [11] Token Joiner        ││ [34] Siren Lookup        ││ [57] Phishing Maker      │  [E] Exit
│ [12] Language changer    ││ [35] Leak Check          ││ [58] Website Link Scrap  │  
│ [13] Token Leaver        ││ [36] Csint Check         ││ [59] UDP Flood           │  [H] Live Support
│ [14] Token Login         ││ [37] Name To Gender      ││ [60] TCP Client          │  
│ [15] Mass DM             ││ [38] Fortnite Lookup     ││ [61] TCP Server          │  
│ [16] Token Nuker         ││ [39] Redline Check       ││ [62] HTTP Flood          │  
│ [17] Token Raider        ││ [40] Xbox Lookup         ││ [63] DoS (DDoS) Layer7   │  
│ [18] Token Spammer       ││ [41] Email Permutator    ││ [64] Proxy Scraper       │  
│ [19] Statut Changer      ││ [42] Document Timeline   ││ [65] Subdomain Scanner   │  
│ [20] ID to Token         ││ [43] Name Footprint      ││ [66] Subdirectory Scanner│  
│ [21] Webhook Deleter     ││ [44] Public Google Drive ││ [67] Port Opener         │  
│ [22] Webhook Spammer     ││ [45] Website Metadata    ││ [68] Fortnite IP Sniffer │  
│ [23] Webhook Info        ││ [46] Instagram Phone Num ││ [69] IP To Domain        │  
└──────────────────────────┘└──────────────────────────┘└──────────────────────────┘    
            
""")

def menu():
    while True:
        os.system('cls')
        print(ascii)
        choice = input(Fore.BLUE + "Beluga@Admin/" + Fore.CYAN + "Root>" + Fore.WHITE)

        if choice in ['E', 'e']:
            exit()

        elif choice in ['I', 'i']:
            os.system('cls')
            script_path = os.path.join('settings', 'About.py')
            if os.path.isfile(script_path):
                subprocess.run(['python', script_path])

        elif choice in ['h', 'H']:
            os.system('cls')
            script_path = os.path.join('Support', 'Support.py')
            if os.path.isfile(script_path):
                subprocess.run(['python', script_path])

        elif choice in ['N', 'n']:
            os.system('cls')
            script_path = os.path.join('settings', 'Pages', '2.py')
            if os.path.isfile(script_path):
                subprocess.run(['python', script_path])

        elif choice == '1':
            os.system('cls')
            script_path = os.path.join('settings', 'Discord', 'Id to bot.py')
            if os.path.isfile(script_path):
                subprocess.run(['python', script_path])

        elif choice =='2':
            os.system('cls')
            script_path = os.path.join('settings','Discord', 'Nuke bot.py')
            if os.path.isfile(script_path):
                subprocess.run(['python', script_path])

        elif choice =='3':
            os.system('cls')
            script_path = os.path.join('settings','Discord', 'Nitro Gen.py')
            if os.path.isfile(script_path):
                subprocess.run(['python', script_path])

        elif choice =='4':
            os.system('cls')
            script_path = os.path.join('settings','Discord', 'Server info.py')
            if os.path.isfile(script_path):
                subprocess.run(['python', script_path])

        elif choice =='5':
            os.system('cls')
            script_path = os.path.join('settings','Discord', 'Token Block.py')
            if os.path.isfile(script_path):
                subprocess.run(['python', script_path])

        elif choice =='6':
            os.system('cls')
            script_path = os.path.join('settings','Discord', 'Dm deleter.py')
            if os.path.isfile(script_path):
                subprocess.run(['python', script_path])

        elif choice =='7':
            os.system('cls')
            script_path = os.path.join('settings','Discord', 'Friends deleter.py')
            if os.path.isfile(script_path):
                subprocess.run(['python', script_path])

        elif choice =='8':
            os.system('cls')
            script_path = os.path.join('settings','Discord', 'Token Gen.py')
            if os.path.isfile(script_path):
                subprocess.run(['python', script_path])

        elif choice =='9':
            os.system('cls')
            script_path = os.path.join('settings','Discord', 'HS Changer.py')
            if os.path.isfile(script_path):
                subprocess.run(['python', script_path])

        elif choice =='10':
            os.system('cls')
            script_path = os.path.join('settings','Discord', 'Token info.py')
            if os.path.isfile(script_path):
                subprocess.run(['python', script_path])

        elif choice =='11':
            os.system('cls')
            script_path = os.path.join('settings','Discord', 'Token joiner.py')
            if os.path.isfile(script_path):
                subprocess.run(['python', script_path])

        elif choice =='12':
            os.system('cls')
            script_path = os.path.join('settings','Discord', 'Langue Changer.py')
            if os.path.isfile(script_path):
                subprocess.run(['python', script_path])

        elif choice =='13':
            os.system('cls')
            script_path = os.path.join('settings','Discord', 'Token Leaver.py')
            if os.path.isfile(script_path):
                subprocess.run(['python', script_path])

        elif choice =='14':
            os.system('cls')
            script_path = os.path.join('settings','Discord', 'Token Login.py')
            if os.path.isfile(script_path):
                subprocess.run(['python', script_path])

        elif choice =='15':
            os.system('cls')
            script_path = os.path.join('settings','Discord', 'Mass DM.py')
            if os.path.isfile(script_path):
                subprocess.run(['python', script_path])

        elif choice =='16':
            os.system('cls')
            script_path = os.path.join('settings','Discord', 'Token Nuker.py')
            if os.path.isfile(script_path):
                subprocess.run(['python', script_path])

        elif choice =='17':
            os.system('cls')
            script_path = os.path.join('settings','Discord', 'Token Raider.py')
            if os.path.isfile(script_path):
                subprocess.run(['python', script_path])

        elif choice =='18':
            os.system('cls')
            script_path = os.path.join('settings','Discord', 'Token Spammer.py')
            if os.path.isfile(script_path):
                subprocess.run(['python', script_path])

        elif choice =='19':
            os.system('cls')
            script_path = os.path.join('settings','Discord', 'Statut changer.py')
            if os.path.isfile(script_path):
                subprocess.run(['python', script_path])

        elif choice =='20':
            os.system('cls')
            script_path = os.path.join('settings','Discord', 'ID to Token.py')
            if os.path.isfile(script_path):
                subprocess.run(['python', script_path])

        elif choice =='21':
            os.system('cls')
            script_path = os.path.join('settings','Discord', 'Webhook Deleter.py')
            if os.path.isfile(script_path):
                subprocess.run(['python', script_path])

        elif choice =='22':
            os.system('cls')
            script_path = os.path.join('settings','Discord', 'Webhook Spammer.py')
            if os.path.isfile(script_path):
                subprocess.run(['python', script_path])

        elif choice =='23':
            os.system('cls')
            script_path = os.path.join('settings','Discord', 'Webhook info.py')
            if os.path.isfile(script_path):
                subprocess.run(['python', script_path])

        elif choice =='24':
            os.system('cls')
            script_path = os.path.join('settings','Osint Csint', 'Dox create.py')
            if os.path.isfile(script_path):
                subprocess.run(['python', script_path])

        elif choice =='25':
            os.system('cls')
            script_path = os.path.join('settings','Osint Csint', 'Ez search.py')
            if os.path.isfile(script_path):
                subprocess.run(['python', script_path])

        elif choice =='26':
            os.system('cls')
            script_path = os.path.join('settings','Osint Csint', 'Email Lookup.py')
            if os.path.isfile(script_path):
                subprocess.run(['python', script_path])

        elif choice =='27':
            os.system('cls')
            script_path = os.path.join('settings','Osint Csint', 'Email Tracker.py')
            if os.path.isfile(script_path):
                subprocess.run(['python', script_path])

        elif choice =='28':
            os.system('cls')
            script_path = os.path.join('settings','Osint Csint', 'Username Tracker.py')
            if os.path.isfile(script_path):
                subprocess.run(['python', script_path])

        elif choice =='29':
            os.system('cls')
            script_path = os.path.join('settings','Osint Csint', 'Free intelX.py')
            if os.path.isfile(script_path):
                subprocess.run(['python', script_path])

        elif choice =='30':
            os.system('cls')
            script_path = os.path.join('settings','Osint Csint', 'Phone Lookup.py')
            if os.path.isfile(script_path):
                subprocess.run(['python', script_path])

        elif choice =='31':
            os.system('cls')
            script_path = os.path.join('settings','Osint Csint', 'Insta Profile viewer.py')
            if os.path.isfile(script_path):
                subprocess.run(['python', script_path])

        elif choice =='32':
            os.system('cls')
            script_path = os.path.join('settings','Osint Csint', 'Osint Beginer.py')
            if os.path.isfile(script_path):
                subprocess.run(['python', script_path])

        elif choice =='33':
            os.system('cls')
            script_path = os.path.join('settings','Osint Csint', 'Image Metadata.py')
            if os.path.isfile(script_path):
                subprocess.run(['python', script_path])

        elif choice =='34':
            os.system('cls')
            script_path = os.path.join('settings','Osint Csint', 'Siren Lookup.py')
            if os.path.isfile(script_path):
                subprocess.run(['python', script_path])

        elif choice =='35':
            os.system('cls')
            script_path = os.path.join('settings','Osint Csint', 'Leak Check.py')
            if os.path.isfile(script_path):
                subprocess.run(['python', script_path])

        elif choice =='36':
            os.system('cls')
            script_path = os.path.join('settings','Osint Csint', 'Csint Check.py')
            if os.path.isfile(script_path):
                subprocess.run(['python', script_path])

        elif choice =='37':
            os.system('cls')
            script_path = os.path.join('settings','Osint Csint', 'Name To Gender.py')
            if os.path.isfile(script_path):
                subprocess.run(['python', script_path])

        elif choice =='38':
            os.system('cls')
            script_path = os.path.join('settings','Osint Csint', 'Fortnite Lookup.py')
            if os.path.isfile(script_path):
                subprocess.run(['python', script_path])
        
        elif choice =='39':
            os.system('cls')
            script_path = os.path.join('settings','Osint Csint', 'Stealer logs Check.py')
            if os.path.isfile(script_path):
                subprocess.run(['python', script_path])

        elif choice =='40':
            os.system('cls')
            script_path = os.path.join('settings','Osint Csint', 'Gamertag to XUID.py')
            if os.path.isfile(script_path):
                subprocess.run(['python', script_path])

        elif choice =='41':
            os.system('cls')
            script_path = os.path.join('settings','Osint Csint', 'Email Permutator.py')
            if os.path.isfile(script_path):
                subprocess.run(['python', script_path])

        elif choice =='42':
            os.system('cls')
            script_path = os.path.join('settings','Osint Csint', 'Document Timeline.py')
            if os.path.isfile(script_path):
                subprocess.run(['python', script_path])

        elif choice =='43':
            os.system('cls')
            script_path = os.path.join('settings','Osint Csint', 'Name Footprint.py')
            if os.path.isfile(script_path):
                subprocess.run(['python', script_path])

        elif choice =='44':
            os.system('cls')
            script_path = os.path.join('settings','Osint Csint', 'Public Google Drive.py')
            if os.path.isfile(script_path):
                subprocess.run(['python', script_path])

        elif choice =='45':
            os.system('cls')
            script_path = os.path.join('settings','Osint Csint', 'Metadata Website.py')
            if os.path.isfile(script_path):
                subprocess.run(['python', script_path])

        elif choice =='46':
            os.system('cls')
            script_path = os.path.join('settings','Osint Csint', 'Instagram Phone Num.py')
            if os.path.isfile(script_path):
                subprocess.run(['python', script_path])
        #======================= 46 / Dox osint =========================





        #======================= 46 / Dox osint =========================

        elif choice =='47':
            os.system('cls')
            script_path = os.path.join('settings','Network', 'IP Gen.py')
            if os.path.isfile(script_path):
                subprocess.run(['python', script_path])

        elif choice =='48':
            os.system('cls')
            script_path = os.path.join('settings','Network', 'IP Lookup.py')
            if os.path.isfile(script_path):
                subprocess.run(['python', script_path])

        elif choice =='49':
            os.system('cls')
            script_path = os.path.join('settings','Network', 'IP Pinger.py')
            if os.path.isfile(script_path):
                subprocess.run(['python', script_path])

        elif choice =='50':
            os.system('cls')
            script_path = os.path.join('settings','Network', 'IP Port Scanner.py')
            if os.path.isfile(script_path):
                subprocess.run(['python', script_path])

        elif choice =='51':
            os.system('cls')
            script_path = os.path.join('settings','Network', 'IP Scanner.py')
            if os.path.isfile(script_path):
                subprocess.run(['python', script_path])

        elif choice =='52':
            os.system('cls')
            script_path = os.path.join('settings','Network', 'Web Scanner.py')
            if os.path.isfile(script_path):
                subprocess.run(['python', script_path])

        elif choice =='53':
            os.system('cls')
            script_path = os.path.join('settings','Network', 'Web Vuln.py')
            if os.path.isfile(script_path):
                subprocess.run(['python', script_path])

        elif choice =='54':
            os.system('cls')
            script_path = os.path.join('settings','Network', 'DDoS ProxySock.py')
            if os.path.isfile(script_path):
                subprocess.run(['python', script_path])

        elif choice =='55':
            os.system('cls')
            script_path = os.path.join('settings','Network', 'Proxy extractor.py')
            if os.path.isfile(script_path):
                subprocess.run(['python', script_path])

        elif choice =='56':
            os.system('cls')
            script_path = os.path.join('settings','Network', 'IP Grabber.py')
            if os.path.isfile(script_path):
                subprocess.run(['python', script_path])

        elif choice =='57':
            os.system('cls')
            script_path = os.path.join('settings','Network', 'Phishing.py')
            if os.path.isfile(script_path):
                subprocess.run(['python', script_path])

        elif choice =='58':
            os.system('cls')
            script_path = os.path.join('settings','Network', 'Link Scrap.py')
            if os.path.isfile(script_path):
                subprocess.run(['python', script_path])

        elif choice =='59':
            os.system('cls')
            script_path = os.path.join('settings','Network', 'UDP Flood.py')
            if os.path.isfile(script_path):
                subprocess.run(['python', script_path])

        elif choice =='60':
            os.system('cls')
            script_path = os.path.join('settings','Network', 'TCP Client.py')
            if os.path.isfile(script_path):
                subprocess.run(['python', script_path])

        elif choice =='61':
            os.system('cls')
            script_path = os.path.join('settings','Network', 'TCP Server.py')
            if os.path.isfile(script_path):
                subprocess.run(['python', script_path])

        elif choice =='62':
            os.system('cls')
            script_path = os.path.join('settings','Network', 'http Flood.py')
            if os.path.isfile(script_path):
                subprocess.run(['python', script_path])

        elif choice =='63':
            os.system('cls')
            script_path = os.path.join('settings','Network', 'DDoS Layer7.py')
            if os.path.isfile(script_path):
                subprocess.run(['python', script_path])

        elif choice =='64':
            os.system('cls')
            script_path = os.path.join('settings','Network', 'ProxyScrap.py')
            if os.path.isfile(script_path):
                subprocess.run(['python', script_path])

        elif choice =='65':
            os.system('cls')
            script_path = os.path.join('settings','Network', 'Subdomaine Scanner.py')
            if os.path.isfile(script_path):
                subprocess.run(['python', script_path])

        elif choice =='66':
            os.system('cls')
            script_path = os.path.join('settings','Network', 'Subdirectory Scanner.py')
            if os.path.isfile(script_path):
                subprocess.run(['python', script_path])

        elif choice =='67':
            os.system('cls')
            script_path = os.path.join('settings','Network', 'Port Opener.py')
            if os.path.isfile(script_path):
                subprocess.run(['python', script_path])

        elif choice =='68':
            os.system('cls')
            script_path = os.path.join('settings','Network', 'Fortnite IP Sniffer.py')
            if os.path.isfile(script_path):
                subprocess.run(['python', script_path])

        elif choice =='69':
            os.system('cls')
            script_path = os.path.join('settings','Network', 'IP To Domain.py')
            if os.path.isfile(script_path):
                subprocess.run(['python', script_path])


if __name__ == "__main__":
    menu()
    