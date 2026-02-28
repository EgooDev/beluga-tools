import re
import unicodedata
from pystyle import Center, Colorate, Colors, Anime
from colorama import Fore
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
def normalize(name):
    if not name: 
        return ""
    nfkd = unicodedata.normalize("NFKD", name)
    cleaned = "".join([c for c in nfkd if not unicodedata.combining(c)])
    cleaned = re.sub(r"[^\w\s\-']", " ", cleaned)
    cleaned = re.sub(r"\s+", " ", cleaned).strip().lower()
    cleaned = cleaned.replace(" ", "").replace("'", "")
    return cleaned

def ask(prompt):
    return input(prompt).strip()

first = ask(Fore.BLUE + "First name: " + Fore.WHITE)
last = ask(Fore.BLUE + "Last name: " + Fore.WHITE)
middle = ask(Fore.BLUE + "Middle name (optional): " + Fore.WHITE)
nickname = ask(Fore.BLUE + "Nickname (optional): " + Fore.WHITE)
domain = ask(Fore.BLUE + "Domain (optional, format: example.com): " + Fore.WHITE)

f = normalize(first)
l = normalize(last)
m = normalize(middle)
n = normalize(nickname)
f1 = f[0] if f else ""
l1 = l[0] if l else ""
m1 = m[0] if m else ""
n1 = n[0] if n else ""

patterns = {
    f,
    l,
    f + l,
    f + "." + l,
    f + "_" + l,
    f + "-" + l,
    l + f,
    f1 + l,
    f + l1,
    f1 + "." + l,
    f + "." + l1,
}

if m:
    patterns.update({
        f + m + l,
        f + "." + m + "." + l,
        f1 + m1 + l1,
        f + m1 + l,
    })

if n:
    patterns.update({
        n,
        n + l,
        f + n + l,
        n + "." + l,
        n + "_" + l
    })

patterns = {p for p in patterns if p}

print("\nGenerated permutations:\n")
for p in sorted(patterns):
    if domain:
        print(f"{p}@{domain.lower()}")
    else:
        print(p)

print(f"\nTotal: {len(patterns)} emails")
input(Fore.RED + "\nPress ENTER to exit...")
