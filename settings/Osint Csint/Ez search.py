from pystyle import Center, Colorate, Colors, Anime
import colorama
import os
import webbrowser

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

def ErrorChoice():
    print(colorama.Fore.RED + "Invalid Choice.")
    exit()

def SearchDox():
    print("""
    [01] Username
    [02] LastName, FirstName
    [03] Other
    """)

    search_type = input("Search Type -> ").strip()

    if search_type in ['1', '01']:
        search = input("Username -> ").strip()
    elif search_type in ['2', '02']:
        name = input("Last Name -> ").strip()
        first_name = input("First Name -> ").strip()
    elif search_type in ['3', '03']:
        search = input("Search -> ").strip()
    else:
        ErrorChoice()

    print("""
    [01] Facebook.com
    [02] Youtube.com
    [03] Twitter.com
    [04] Tiktok.com
    [05] Peekyou.com
    [06] Tumblr.com
    [07] PagesJaunes.fr
    [00] Exit
    """)

    while True:
        choice = input("Site -> ").strip()

        if choice in ['0', '00']:
            break

        elif choice in ['01', '1']:
            if search_type in ['01', '1', '03', '3']:
                webbrowser.open(f"https://www.facebook.com/search/top/?q={search}")
            elif search_type in ['02', '2']:
                webbrowser.open(f"https://www.facebook.com/search/top/?q={name}%20{first_name}")

        elif choice in ['02', '2']:
            if search_type in ['01', '1', '03', '3']:
                webbrowser.open(f"https://www.youtube.com/results?search_query={search}")
            elif search_type in ['02', '2']:
                webbrowser.open(f"https://www.youtube.com/results?search_query={name}+{first_name}")

        elif choice in ['03', '3']:
            if search_type in ['01', '1', '03', '3']:
                webbrowser.open(f"https://twitter.com/search?q={search}")
            elif search_type in ['02', '2']:
                webbrowser.open(f"https://twitter.com/search?q={name}%20{first_name}")

        elif choice in ['04', '4']:
            if search_type in ['01', '1', '03', '3']:
                webbrowser.open(f"https://www.tiktok.com/search?q={search}")
            elif search_type in ['02', '2']:
                webbrowser.open(f"https://www.tiktok.com/search?q={name}%20{first_name}")

        elif choice in ['05', '5']:
            if search_type in ['01', '1', '03', '3']:
                webbrowser.open(f"https://www.peekyou.com/{search}")
            elif search_type in ['02', '2']:
                webbrowser.open(f"https://www.peekyou.com/{name}_{first_name}")

        elif choice in ['06', '6']:
            if search_type in ['01', '1', '03', '3']:
                webbrowser.open(f"https://www.tumblr.com/search/{search}")
            elif search_type in ['02', '2']:
                webbrowser.open(f"https://www.tumblr.com/search/{name}%20{first_name}")

        elif choice in ['07', '7']:
            if search_type in ['01', '1', '03', '3']:
                webbrowser.open(f"https://www.pagesjaunes.fr/pagesblanches/recherche?quoiqui={search}")
            elif search_type in ['02', '2']:
                webbrowser.open(f"https://www.pagesjaunes.fr/pagesblanches/recherche?quoiqui={name}%20{first_name}")

        else:
            ErrorChoice()

try:
    SearchDox()
except Exception as e:
    print(colorama.Fore.RED + f"Error: {e}")
