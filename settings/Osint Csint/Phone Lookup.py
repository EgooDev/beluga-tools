import phonenumbers
from phonenumbers import geocoder, carrier
import math
import socket
import colorama
from colorama import Fore
import os
import subprocess
import time
import webbrowser
import threading
from pystyle import Center, Colorate, Colors, Anime
import colorama
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
def analyze_number(phone_number):
    try:
        parsed_number = phonenumbers.parse(phone_number)

        formatted_international = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        formatted_national = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.NATIONAL)

        valid = phonenumbers.is_valid_number(parsed_number)
        possible = phonenumbers.is_possible_number(parsed_number)

        country_code = geocoder.region_code_for_number(parsed_number)
        country_description = geocoder.description_for_number(parsed_number, "fr")

        carrier_name = carrier.name_for_number(parsed_number, 'fr')

        number_type = phonenumbers.number_type(parsed_number)


        print(Fore.WHITE + f"Numéro formaté (international) : {formatted_international}")
        print(f"Numéro formaté (national) : {formatted_national}")
        print(f"Validité : {valid}")
        print(f"Possibilité : {possible}")
        print(f"Code du pays : {country_code}")
        print(f"Description du pays : {country_description}")
        print(f"Opérateur : {carrier_name}")


        if number_type == phonenumbers.PhoneNumberType.MOBILE:
            print("Type : Mobile")
        elif number_type == phonenumbers.PhoneNumberType.FIXED_LINE:
            print("Type : Fixe")
        elif number_type == phonenumbers.PhoneNumberType.TOLL_FREE:
            print("Type : Numéro gratuit")
        elif number_type == phonenumbers.PhoneNumberType.PREMIUM_RATE:
            print("Type : Numéro surtaxé")
        elif number_type == phonenumbers.PhoneNumberType.VOIP:
            print("Type : VoIP")
        elif number_type == phonenumbers.PhoneNumberType.UNKNOWN:
            print("Type : Inconnu")
        else:
            print("Type : Autre")

    except phonenumbers.NumberParseException:
        print(Fore.RED + "invalid")
    except Exception as e:
        print(Fore.RED + f"Erreur{e}")

if __name__ == "__main__":
    user_input = input(Fore.CYAN + "Phone Number: " + Fore.BLUE)
    analyze_number(user_input)
    input(Fore.RED + "PRESS ENTER TO EXIT...")
