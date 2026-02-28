import requests
import json
import re
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
    "User-Agent": "Mozilla/5.0 (OSINT Name Footprint Beluga)"
}

SOCIAL_NETWORKS = {
    "LinkedIn": "https://www.linkedin.com/search/results/all/?keywords={}",
    "Facebook": "https://www.facebook.com/search/top?q={}",
    "Twitter/X": "https://twitter.com/search?q={}&src=typed_query",
    "Instagram": "https://www.instagram.com/web/search/topsearch/?query={}",
    "GitHub": "https://github.com/search?q={}",
}

DOCUMENT_SOURCES = {
    "Google PDF": 'https://www.google.com/search?q="{}"+filetype:pdf',
    "Google DOC": 'https://www.google.com/search?q="{}"+filetype:doc',
    "Google CV": 'https://www.google.com/search?q="{}"+CV',
}

SEARCH_ENGINES = {
    "Google": 'https://www.google.com/search?q="{}"',
    "Bing": 'https://www.bing.com/search?q="{}"',
    "DuckDuckGo": 'https://duckduckgo.com/?q="{}"',
}

def generate_queries(full_name):
    queries = []

    for engine, url in SEARCH_ENGINES.items():
        queries.append({
            "type": "Search Engine",
            "platform": engine,
            "query": url.format(quote(full_name))
        })

    for platform, url in SOCIAL_NETWORKS.items():
        queries.append({
            "type": "Social Network",
            "platform": platform,
            "query": url.format(quote(full_name))
        })

    for source, url in DOCUMENT_SOURCES.items():
        queries.append({
            "type": "Document Search",
            "platform": source,
            "query": url.format(quote(full_name))
        })

    return queries

def passive_check(url):
    try:
        r = requests.get(url, headers=HEADERS, timeout=5)
        if r.status_code == 200:
            return "POSSIBLE HIT"
        return "NO SIGNAL"
    except:
        return "ERROR"

def footprint(full_name):
    print(f"\nWait..Search: {full_name}")
    print("🟢: SIGNAL | ⚪ NO SIGNAL")
    queries = generate_queries(full_name)
    results = []

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = []
        for q in queries:
            futures.append(executor.submit(passive_check, q["query"]))

        for q, f in zip(queries, futures):
            status = f.result()
            signal = "🟢" if status == "POSSIBLE HIT" else "⚪"
            print(f"{signal} [{q['type']}] {q['platform']}")
            print(f"    ↳ {q['query']}")
            results.append({
                "type": q["type"],
                "platform": q["platform"],
                "url": q["query"],
                "status": status
            })

if __name__ == "__main__":
    name = input("Enter a full name to search: ").strip()
    footprint(name)
    input("\nPress enter to exit...")
