import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import os
import sys
from PIL import Image
from PIL.ExifTags import TAGS
from pystyle import Center, Colorate, Colors, Anime
from colorama import Fore
import os

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
HEADERS = {
    "User-Agent": "Metadata Website Scraper"
}

KNOWN_TRACKERS = [
    "google-analytics.com",
    "googletagmanager.com",
    "facebook.net",
    "hotjar.com",
    "clarity.ms",
    "segment.com",
    "mixpanel.com",
    "cdn.amplitude.com",
    "matomo",
    "cloudflareinsights.com"
]

def scrape_metadata(url):
    print(f"\nMetadata Website Scraper")
    print(f"URL : {url}\n")

    r = requests.get(url, headers=HEADERS, timeout=8)
    soup = BeautifulSoup(r.text, "html.parser")

    # Title
    print("Title")
    title = soup.title.string.strip() if soup.title else None
    print(f"  {title}\n")

    # Meta tags
    print("Meta tags")
    metas = soup.find_all("meta")
    for m in metas:
        name = m.get("name") or m.get("property")
        content = m.get("content")
        if name and content:
            print(f"  {name} → {content}")

    print("")

    # Scripts
    print("Scripts")
    scripts = soup.find_all("script", src=True)
    for s in scripts:
        print(f"  {s['src']}")

    print("")

    # Trackers
    print("Trackers détectés")
    parsed = urlparse(url)
    found = set()

    for s in scripts:
        src = s["src"]
        for tracker in KNOWN_TRACKERS:
            if tracker in src:
                found.add(tracker)

    for t in found:
        print(f"  {t}")

    if not found:
        print("No known trackers detected")

if __name__ == "__main__":
    target_url = input("Url of Website: ").strip()
    scrape_metadata(target_url)
    input("Press enter to exit..")
