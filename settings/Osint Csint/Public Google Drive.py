import requests
import json
from urllib.parse import quote
from concurrent.futures import ThreadPoolExecutor
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
    "User-Agent": "OSINT Public Exposure Finder"
}

KEYWORDS = [
    "backup", "password", "credentials", "confidential",
    "invoice", "client", "database", "export", "internal"
]

GOOGLE_DRIVE_QUERIES = {
    "Drive Folder": 'https://www.google.com/search?q=site:drive.google.com+"{}"',
    "Drive File": 'https://www.google.com/search?q=site:drive.google.com/file+"{}"',
    "Google Docs": 'https://www.google.com/search?q=site:docs.google.com+"{}"',
}

S3_QUERIES = {
    "S3 Bucket (global)": 'https://www.google.com/search?q=site:s3.amazonaws.com+"{}"',
    "S3 Bucket (region)": 'https://www.google.com/search?q=site:s3.*.amazonaws.com+"{}"',
    "S3 Index Listing": 'https://www.google.com/search?q=intitle:"index of"+s3.amazonaws.com+"{}"',
}

def generate_queries(target):
    queries = []

    for name, q in GOOGLE_DRIVE_QUERIES.items():
        queries.append({
            "category": "Google Drive",
            "technique": name,
            "url": q.format(quote(target))
        })

    for name, q in S3_QUERIES.items():
        queries.append({
            "category": "AWS S3",
            "technique": name,
            "url": q.format(quote(target))
        })

    for keyword in KEYWORDS:
        queries.append({
            "category": "Keyword Search",
            "technique": f'Keyword "{keyword}"',
            "url": f'https://www.google.com/search?q="{quote(target)}"+{keyword}'
        })

    return queries

def check_access(url):
    try:
        r = requests.get(url, headers=HEADERS, timeout=6)
        return r.status_code
    except:
        return None

def run_finder(target):
    print(f"Target : {target}\n")

    queries = generate_queries(target)
    results = []

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(check_access, q["url"]) for q in queries]

        for q, f in zip(queries, futures):
            status = f.result()
            print(f"[{q['category']}] {q['technique']}")
            print(f"  ↳ {q['url']} (HTTP: {status})")

            results.append({
                "category": q["category"],
                "technique": q["technique"],
                "url": q["url"],
                "http_status": status
            })


target = input("Name of company: ").strip()
run_finder(target)
input("Press enter to exit...")
