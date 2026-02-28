from pystyle import Center, Colorate, Colors, Anime
import colorama
import os
import dns.resolver
import re

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

def get_email_info(email):
    info = {}
    
    try:
        domain_all = email.split('@')[-1]
    except:
        domain_all = None

    try:
        name = email.split('@')[0]
    except:
        name = None

    try:
        domain = re.search(r"@([^@.]+)\.", email).group(1)
    except:
        domain = None

    try:
        tld = f".{email.split('.')[-1]}"
    except:
        tld = None

    try:
        mx_records = dns.resolver.resolve(domain_all, 'MX')
        mx_servers = [str(record.exchange) for record in mx_records]
        info["mx_servers"] = mx_servers
    except:
        info["mx_servers"] = None

    try:
        spf_records = dns.resolver.resolve(domain_all, 'SPF')
        info["spf_records"] = [str(record) for record in spf_records]
    except:
        info["spf_records"] = None

    try:
        dmarc_records = dns.resolver.resolve(f'_dmarc.{domain_all}', 'TXT')
        info["dmarc_records"] = [str(record) for record in dmarc_records]
    except:
        info["dmarc_records"] = None

    if info.get("mx_servers"):
        for server in info["mx_servers"]:
            if "google.com" in server:
                info["google_workspace"] = True
            elif "outlook.com" in server:
                info["microsoft_365"] = True

    return info, domain_all, domain, tld, name

try:
    email = input(colorama.Fore.CYAN + "\n[+] Email -> " + colorama.Fore.RESET)
    print(colorama.Fore.YELLOW + "[*] Récupération des informations..." + colorama.Fore.RESET)

    info, domain_all, domain, tld, name = get_email_info(email)

    mx_servers = ' / '.join(info["mx_servers"]) if info["mx_servers"] else "None"
    spf_records = ' / '.join(info["spf_records"]) if info["spf_records"] else "None"
    dmarc_records = ' / '.join(info["dmarc_records"]) if info["dmarc_records"] else "None"
    google_workspace = info.get("google_workspace", "False")

    print(colorama.Fore.GREEN + f"""
    [+] Email      : {email}
    [+] Name       : {name}
    [+] Domain     : {domain}
    [+] TLD        : {tld}
    [+] Domain All : {domain_all}
    [+] Servers    : {mx_servers}
    [+] SPF        : {spf_records}
    [+] DMARC      : {dmarc_records}
    [+] Workspace  : {google_workspace}
    """ + colorama.Fore.RESET)
    input(" ")

except Exception as e:
    print(colorama.Fore.RED + f"[!] Erreur : {e}" + colorama.Fore.RESET)
