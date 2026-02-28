import socket
from pystyle import Center, Colorate, Colors
import os
from colorama import Fore

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
def portopener():
    port = int(input("Enter the port to open (between 1024 and 65535): "))
    serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serveur.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        serveur.bind(("0.0.0.0", port))
        serveur.listen(5)
        print(f"Port {port} open and listening (Ctrl+C to stop).")

        while True:
            client, address = serveur.accept()
            print(f"Connection received from {address}")
            client.send(b"Hello, connection successful!\n")
            client.close()

    except PermissionError:
        print("Error: insufficient privileges (port < 1024 requires administrator rights).")
    except OSError as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("\nServer stopped.")
    finally:
        serveur.close()

portopener()
input(Fore.RED + "Press Enter to exit...")
