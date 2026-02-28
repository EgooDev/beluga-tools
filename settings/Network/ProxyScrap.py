import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import re
from colorama import Fore, Style
from pystyle import Center, Colorate, Colors, Anime
import os
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
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

def get_proxyscrape():
    url = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=5000&country=all"
    try:
        res = requests.get(url, headers=HEADERS, timeout=10)
        return res.text.strip().splitlines()
    except:
        return []

def get_free_proxy_list():
    url = "https://free-proxy-list.net/"
    proxies = []
    try:
        res = requests.get(url, headers=HEADERS, timeout=10)
        soup = BeautifulSoup(res.text, 'lxml')
        rows = soup.select("table#proxylisttable tbody tr")
        for row in rows:
            cols = row.find_all("td")
            if cols[6].text.strip() == "yes":  
                ip = cols[0].text.strip()
                port = cols[1].text.strip()
                proxies.append(f"{ip}:{port}")
    except:
        pass
    return proxies

def get_geonode():
    url = "https://proxylist.geonode.com/api/proxy-list?limit=100&page=1&sort_by=lastChecked&sort_type=desc"
    proxies = []
    try:
        res = requests.get(url, headers=HEADERS, timeout=10)
        data = res.json()
        for proxy in data.get("data", []):
            ip = proxy.get("ip")
            port = proxy.get("port")
            if ip and port:
                proxies.append(f"{ip}:{port}")
    except:
        pass
    return proxies

def get_free_proxy_cz():
    url = "http://free-proxy.cz/en/"
    proxies = []
    try:
        res = requests.get(url, headers=HEADERS, timeout=10)
        soup = BeautifulSoup(res.text, 'lxml')
        rows = soup.select("table#proxy_list tbody tr")
        for row in rows:
            script = row.find("script")
            if script:
                match = re.search(r'Base64.decode\("(.+?)"\)', script.string)
                if match:
                    ip_encoded = match.group(1)
                    ip = requests.utils.unquote(
                        requests.utils.base64.b64decode(ip_encoded).decode()
                    )
                    port = row.find_all("td")[1].text.strip()
                    proxies.append(f"{ip}:{port}")
    except:
        pass
    return proxies

def check_proxy(proxy):
    try:
        res = requests.get("http://httpbin.org/ip", proxies={"http": f"http://{proxy}", "https": f"http://{proxy}"}, timeout=5)
        if res.status_code == 200:
            return proxy
    except:
        return None

def save_proxies(valid_proxies):
    with open("Proxy.txt", "w") as f:
        for proxy in valid_proxies:
            f.write(proxy + "\n")

def main():
    print("🔍 Scraping proxies...")
    proxies = set()
    proxies.update(get_proxyscrape())
    proxies.update(get_free_proxy_list())
    proxies.update(get_geonode())
    proxies.update(get_free_proxy_cz())

    print(f"🌐 Total proxies found: {len(proxies)}")

    print("⚙️ Checking proxies (this can take a while)...")
    valid = []
    with ThreadPoolExecutor(max_workers=50) as executor:
        results = list(executor.map(check_proxy, proxies))
        valid = [proxy for proxy in results if proxy]

    print(f"✅ Working proxies: {len(valid)}")
    save_proxies(valid)
    print("📁 Saved to Proxy.txt")

if __name__ == "__main__":
    main()
