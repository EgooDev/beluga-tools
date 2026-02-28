import requests
from pystyle import Center, Colorate, Colors, Anime
import colorama
import os
from datetime import datetime, timezone

def check_token(token):
    url = "https://discord.com/api/v9/users/@me"
    headers = {
        "Authorization": token
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        user = response.json()
        print(f"✅ Token valide : {token}")
        print(f"   → Utilisateur : {user['username']}#{user['discriminator']}")
    elif response.status_code == 401:
        print(f"❌ Token invalide : {token}")
    else:
        print(f"⚠️ Erreur inconnue (code {response.status_code}) pour le token : {token}")

def lire_tokens_fichier(chemin):
    tokens = []
    try:
        with open(chemin, 'r', encoding='utf-8') as f:
            for ligne in f:
                ligne = ligne.strip()
                if ligne:
                    tokens.append(ligne)
    except Exception as e:
        print(f"Erreur de lecture du fichier {chemin} : {e}")
    return tokens

def recuperer_tous_les_tokens():
    tokens = []

    dossier = "input"
    if os.path.exists(dossier):
        for fichier in os.listdir(dossier):
            chemin_complet = os.path.join(dossier, fichier)
            if os.path.isfile(chemin_complet):
                tokens += lire_tokens_fichier(chemin_complet)

    if os.path.isfile("tokens.txt"):
        tokens += lire_tokens_fichier("tokens.txt")

    return tokens

os.system('cls' if os.name == 'nt' else 'clear')
print(Colorate.Vertical(Colors.yellow_to_red,"""
                                                                    
                    (       (                   )\ )         (     
                     ( )\    ( )\  (  (  (     )  (()/(   ) (   )\ )  
                    )((_)  ))((_)))\ )\))( ( /(   /(_)| /( )\ (()/(  
                   ((_)_  /((_) /((_|(_))\ )(_)) (_)) )(_)|(_) ((_)) 
                    | _ )(_))| (_))( (()(_|(_)_  | _ ((_)_ (_) _| |  
                    | _ \/ -_) | || / _` |/ _` | |   / _` || / _` |  
                    |___/\___|_|\_,_\__, |\__,_| |_|_\__,_||_\__,_|  
                                     |___/     
                                               
                               ┏━━━━━━━━━━━━━━━━━━━━━┓
                               ┃  Author : Ego/xhe   ┃
                               ┃ Discord: .gg/xxxx   ┃
                               ┗━━━━━━━━━━━━━━━━━━━━━┛    
"""))

if __name__ == "__main__":
    tokens = recuperer_tous_les_tokens()

    if not tokens:
        print("⚠️ Aucun token trouvé dans 'input/' ou 'tokens.txt'.")
    else:
        print(f"🔎 {len(tokens)} token(s) trouvé(s), vérification en cours...\n")
        for token in tokens:
            check_token(token.strip())
