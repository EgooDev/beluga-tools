import random
import string
import os
from colorama import Fore, Back, Style, init
import requests
from pystyle import Colors, Colorate
import time
from pystyle import Center, Colorate, Colors, Anime
from colorama import Fore
import os


init(autoreset=True)

def generate_random_credit_card(brand):
    if brand == "Visa":
        card_number = '4' + ''.join(random.choice(string.digits) for _ in range(15))
    elif brand == "MasterCard":
        card_number = '5' + ''.join(random.choice(string.digits) for _ in range(15)) 
    return card_number

def generate_random_expiry_date():
    month = random.randint(1, 12)
    year = random.randint(2025, 2030)
    return f"{month:02}/{year}"

def generate_random_cvv():
    return ''.join(random.choice(string.digits) for _ in range(3))

def luhn(n):
    r = [int(ch) for ch in str(n)][::-1]
    return (sum(r[0::2]) + sum(sum(divmod(d*2, 10)) for d in r[1::2])) % 10 == 0

def main():


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

    try:
        number_of_cards = int(input(Colorate.Horizontal(Colors.blue_to_cyan, "How many card: ")))
    except ValueError:
        print(Fore.RED + "Please enter a valid number.")
        return

    choice = input(Colorate.Horizontal(Colors.purple_to_blue, "Would you like to see the results in the terminal (T) or send them to a Discord webhook (W)? (T/W)").strip().lower())

    if choice == 'w':
        discord_webhook = input(Fore.MAGENTA + "Webhook URL: ").strip()

    folder_name = "Data"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    brands = ["Visa", "MasterCard"]

    valid_file_path = os.path.join(folder_name, "Beluga - Valid Card.txt")
    invalid_file_path = os.path.join(folder_name, "Beluga - Invalid Card.txt")

    with open(valid_file_path, "a") as valid_file, open(invalid_file_path, "a") as invalid_file:
        try:
            for _ in range(number_of_cards):
                brand = random.choice(brands)
                card_number = generate_random_credit_card(brand)
                expiry_date = generate_random_expiry_date()
                cvv = generate_random_cvv()
                is_valid = luhn(card_number)  
                status = "Valid" if is_valid else "Invalid"
                result = f"{status} - {card_number} ({brand}) - Exp: {expiry_date} - CVV: {cvv}\n"

                if is_valid:
                    valid_file.write(result)
                    if choice == 't':
                        print(Colorate.Horizontal(Colors.green_to_cyan, result.strip()))
                else:
                    invalid_file.write(result)
                    if choice == 't':
                        print(Colorate.Horizontal(Colors.purple_to_red, result.strip()))

                if choice == 'w' and discord_webhook:
                    data = {"content": result.strip()}
                    requests.post(discord_webhook, json=data)

        except KeyboardInterrupt:
            print(Colorate.Horizontal(Colors.purple_to_red, "\nExiting..."))

if __name__ == "__main__":
    main()
    time.sleep(10)
