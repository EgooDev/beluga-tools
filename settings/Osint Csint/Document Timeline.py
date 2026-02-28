import os
import re
import docx
import dateparser
from pdfminer.high_level import extract_text as extract_pdf_text
from pystyle import Center, Colorate, Colors, Anime
from colorama import Fore

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
def extract_text_from_file(file_path):
    ext = file_path.lower()
    if ext.endswith(".docx"):
        doc = docx.Document(file_path)
        return "\n".join([p.text for p in doc.paragraphs])
    elif ext.endswith(".txt"):
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    elif ext.endswith(".pdf"):
        try:
            return extract_pdf_text(file_path)
        except Exception as e:
            print(f"[ERROR] Could not read PDF {file_path}: {e}")
            return ""
    else:
        return ""

def extract_dates(text):
    date_patterns = [
        r"\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b",
        r"\b\d{4}[/-]\d{1,2}[/-]\d{1,2}\b",
        r"\b\d{1,2}\s+[A-Za-zéû]+\s+\d{4}\b"
    ]
    matches = []
    for pattern in date_patterns:
        matches += re.findall(pattern, text)
    parsed_dates = []
    for m in matches:
        dt = dateparser.parse(m, languages=['en', 'fr'])
        if dt:
            parsed_dates.append(dt.date())
    return parsed_dates

folder_input = input(Fore.BLUE + "Enter Folder Path: " + Fore.WHITE)
folder_path = folder_input.replace("&", "").strip().strip("'\"")

if not os.path.isdir(folder_path):
    print(Fore.RED + "[ERROR] Folder not found!")
    exit()

print(f"\n[INFO] Processing folder: {folder_path}\n")

found_file = False
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if not filename.lower().endswith((".docx", ".txt", ".pdf")):
        continue  

    found_file = True
    text = extract_text_from_file(file_path)
    if not text:
        continue

    dates = extract_dates(text)
    print(f"File: {filename}")
    if dates:
        for d in sorted(dates):
            print(f" - {d}")
    else:
        print(" - No dates found")
    print("-" * 40)

if not found_file:
    print("[INFO] No DOCX, TXT, or PDF files found in this folder.")

input(Fore.RED + "Press Enter to exit...")
