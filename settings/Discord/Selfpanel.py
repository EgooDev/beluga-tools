import sys
import requests
import json
import threading
import os
from time import sleep
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit,
    QPushButton, QTextEdit, QStackedWidget, QInputDialog
)
os.system("pip uninstall discord.py")
os.system("pip install discord.py==1.7.1")


BASE_URL = "https://discord.com/api/v10"

class TokenWindow(QWidget):
    def __init__(self, on_token_entered):
        super().__init__()
        self.on_token_entered = on_token_entered
        self.setWindowTitle("Connexion Selfbot")

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Entrez votre token utilisateur Discord :"))

        self.token_input = QLineEdit()
        self.token_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.token_input)

        self.confirm_btn = QPushButton("Se connecter")
        self.confirm_btn.clicked.connect(self.handle_token)
        layout.addWidget(self.confirm_btn)

        self.setLayout(layout)

    def handle_token(self):
        token = self.token_input.text().strip()
        if token:
            self.on_token_entered(token)

class SelfbotInterface(QWidget):
    def __init__(self, token):
        super().__init__()
        self.token = token
        self.setWindowTitle("Selfbot Discord")

        layout = QVBoxLayout()
        layout.addWidget(QLabel("🧠 Connecté en tant que selfbot."))

        # Message dans un channel
        self.channel_input = QLineEdit()
        self.channel_input.setPlaceholderText("ID du channel")

        self.message_input = QLineEdit()
        self.message_input.setPlaceholderText("Message à envoyer")

        self.send_channel_btn = QPushButton("📢 Envoyer dans un channel")
        self.send_channel_btn.clicked.connect(self.send_message_to_channel)

        layout.addWidget(self.channel_input)
        layout.addWidget(self.message_input)
        layout.addWidget(self.send_channel_btn)

        # Spam
        self.repeat_count_input = QLineEdit()
        self.repeat_count_input.setPlaceholderText("Combien de fois envoyer")

        self.delay_input = QLineEdit()
        self.delay_input.setPlaceholderText("Délai entre messages (secondes)")

        self.spam_btn = QPushButton("🔁 Spam contrôlé")
        self.spam_btn.clicked.connect(self.spam_channel)

        layout.addWidget(self.repeat_count_input)
        layout.addWidget(self.delay_input)
        layout.addWidget(self.spam_btn)

        # DM à un user
        self.user_dm_input = QLineEdit()
        self.user_dm_input.setPlaceholderText("ID de l'utilisateur")

        self.dm_message_input = QLineEdit()
        self.dm_message_input.setPlaceholderText("Message privé")

        self.dm_button = QPushButton("💬 Envoyer un DM")
        self.dm_button.clicked.connect(self.send_dm)

        layout.addWidget(self.user_dm_input)
        layout.addWidget(self.dm_message_input)
        layout.addWidget(self.dm_button)

        # DM multiple
        self.mass_dm_users_input = QLineEdit()
        self.mass_dm_users_input.setPlaceholderText("IDs utilisateurs séparés par virgules")

        self.mass_dm_msg_input = QLineEdit()
        self.mass_dm_msg_input.setPlaceholderText("Message à envoyer à tous")

        self.mass_dm_btn = QPushButton("📤 DM à plusieurs")
        self.mass_dm_btn.clicked.connect(self.send_mass_dm)

        layout.addWidget(self.mass_dm_users_input)
        layout.addWidget(self.mass_dm_msg_input)
        layout.addWidget(self.mass_dm_btn)

        # Groupe MP
        self.group_input = QLineEdit()
        self.group_input.setPlaceholderText("IDs utilisateurs pour groupe MP")

        self.group_btn = QPushButton("👥 Créer un groupe MP")
        self.group_btn.clicked.connect(self.create_group_dm)

        layout.addWidget(self.group_input)
        layout.addWidget(self.group_btn)

        # Multi Groupes
        self.multi_group_input = QLineEdit()
        self.multi_group_input.setPlaceholderText("IDs utilisateurs pour multi-groupe")

        self.group_count_input = QLineEdit()
        self.group_count_input.setPlaceholderText("Nombre de groupes à créer")

        self.multi_group_btn = QPushButton("🔁 Créer plusieurs groupes")
        self.multi_group_btn.clicked.connect(self.create_multiple_groups)

        layout.addWidget(self.multi_group_input)
        layout.addWidget(self.group_count_input)
        layout.addWidget(self.multi_group_btn)

        # Quitter groupes spécifiques
        self.leave_group_input = QLineEdit()
        self.leave_group_input.setPlaceholderText("IDs des groupes à quitter (virgule)")
        self.leave_group_btn = QPushButton("🚪 Quitter les groupes choisis")
        self.leave_group_btn.clicked.connect(self.leave_selected_groups)
        layout.addWidget(self.leave_group_input)
        layout.addWidget(self.leave_group_btn)

        # DM à tout un serveur
        self.server_id_input = QLineEdit()
        self.server_id_input.setPlaceholderText("ID du serveur")

        self.server_dm_msg_input = QLineEdit()
        self.server_dm_msg_input.setPlaceholderText("Message à envoyer à tous les membres")

        self.server_dm_btn = QPushButton("📬 DM à tout le serveur")
        self.server_dm_btn.clicked.connect(self.send_server_dm)

        layout.addWidget(self.server_id_input)
        layout.addWidget(self.server_dm_msg_input)
        layout.addWidget(self.server_dm_btn)

        # Log
        self.output = QTextEdit()
        self.output.setReadOnly(True)
        layout.addWidget(QLabel("📄 Journal :"))
        layout.addWidget(self.output)

        self.setLayout(layout)

    def get_headers(self):
        return {
            "Authorization": self.token,
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0",
        }

    def log(self, msg):
        self.output.append(msg)

    def send_message_to_channel(self):
        channel_id = self.channel_input.text().strip()
        content = self.message_input.text().strip()

        if not channel_id or not content:
            self.log("⚠️ Remplis les champs pour le message dans le channel.")
            return

        res = requests.post(
            f"{BASE_URL}/channels/{channel_id}/messages",
            headers=self.get_headers(),
            json={"content": content}
        )

        if res.status_code == 200:
            self.log("✅ Message envoyé dans le channel.")
        else:
            self.log(f"❌ Erreur : {res.status_code} - {res.text}")

    def spam_channel(self):
        channel_id = self.channel_input.text().strip()
        content = self.message_input.text().strip()

        try:
            repeat = int(self.repeat_count_input.text().strip())
            delay = float(self.delay_input.text().strip())
        except:
            self.log("⚠️ Nombre de répétitions ou délai invalide.")
            return

        def spam():
            for i in range(repeat):
                res = requests.post(
                    f"{BASE_URL}/channels/{channel_id}/messages",
                    headers=self.get_headers(),
                    json={"content": content}
                )
                if res.status_code == 200:
                    self.log(f"✅ Message {i+1}/{repeat} envoyé")
                else:
                    self.log(f"❌ Erreur {i+1} : {res.status_code}")
                sleep(delay)

        threading.Thread(target=spam).start()

    def send_dm(self):
        user_id = self.user_dm_input.text().strip()
        content = self.dm_message_input.text().strip()

        if not user_id or not content:
            self.log("⚠️ Remplis les champs pour le DM.")
            return

        dm_res = requests.post(
            f"{BASE_URL}/users/@me/channels",
            headers=self.get_headers(),
            json={"recipient_id": user_id}
        )

        if dm_res.status_code == 200:
            ch_id = dm_res.json()["id"]
            msg_res = requests.post(
                f"{BASE_URL}/channels/{ch_id}/messages",
                headers=self.get_headers(),
                json={"content": content}
            )
            if msg_res.status_code == 200:
                self.log("✅ DM envoyé.")
            else:
                self.log(f"❌ Erreur en envoyant le DM : {msg_res.text}")
        else:
            self.log(f"❌ Impossible de créer le DM : {dm_res.text}")

    def send_mass_dm(self):
        users = self.mass_dm_users_input.text().strip().split(",")
        message = self.mass_dm_msg_input.text().strip()
        if not users or not message:
            self.log("⚠️ Remplis tous les champs pour le DM multiple.")
            return

        def mass_send():
            for uid in users:
                uid = uid.strip()
                dm_res = requests.post(
                    f"{BASE_URL}/users/@me/channels",
                    headers=self.get_headers(),
                    json={"recipient_id": uid}
                )
                if dm_res.status_code == 200:
                    ch_id = dm_res.json()["id"]
                    msg_res = requests.post(
                        f"{BASE_URL}/channels/{ch_id}/messages",
                        headers=self.get_headers(),
                        json={"content": message}
                    )
                    if msg_res.status_code == 200:
                        self.log(f"✅ Message envoyé à {uid}")
                    else:
                        self.log(f"❌ Erreur envoi à {uid}")
                else:
                    self.log(f"❌ Impossible de créer DM avec {uid}")

        threading.Thread(target=mass_send).start()

    def create_group_dm(self):
        ids = self.group_input.text().strip().split(",")
        user_ids = [uid.strip() for uid in ids if uid.strip()]
        if not user_ids:
            self.log("⚠️ Aucune ID valide pour créer un groupe.")
            return

        res = requests.post(
            f"{BASE_URL}/users/@me/channels",
            headers=self.get_headers(),
            json={"recipients": user_ids}
        )

        if res.status_code == 200:
            self.log(f"✅ Groupe MP créé avec {', '.join(user_ids)}")
        else:
            self.log(f"❌ Erreur création groupe : {res.text}")

    def create_multiple_groups(self):
        ids = self.multi_group_input.text().strip().split(",")
        user_ids = [uid.strip() for uid in ids if uid.strip()]
        try:
            count = int(self.group_count_input.text().strip())
        except ValueError:
            self.log("⚠️ Le nombre de groupes n'est pas valide.")
            return

        for i in range(count):
            res = requests.post(
                f"{BASE_URL}/users/@me/channels",
                headers=self.get_headers(),
                json={"recipients": user_ids}
            )
            if res.status_code == 200:
                self.log(f"✅ Groupe {i+1}/{count} créé.")
            else:
                self.log(f"❌ Groupe {i+1} échoué : {res.text}")

    def leave_selected_groups(self):
        group_ids = self.leave_group_input.text().strip().split(",")
        group_ids = [gid.strip() for gid in group_ids if gid.strip()]

        if not group_ids:
            self.log("⚠️ Aucun ID de groupe fourni.")
            return

        for gid in group_ids:
            del_res = requests.delete(f"{BASE_URL}/channels/{gid}", headers=self.get_headers())
            if del_res.status_code == 200:
                self.log(f"✅ Groupe {gid} quitté.")
            else:
                self.log(f"❌ Erreur en quittant {gid} : {del_res.text}")

    def send_server_dm(self):
        server_id = self.server_id_input.text().strip()
        message = self.server_dm_msg_input.text().strip()

        if not server_id or not message:
            self.log("⚠️ Fournis l'ID du serveur et le message.")
            return

        # Demander un salon texte visible pour contourner l'erreur 50001
        channel_id, ok = QInputDialog.getText(self, "Salon visible requis",
                                              "Entrez un ID de salon texte du serveur :")
        if not ok or not channel_id.strip():
            self.log("❌ Aucun salon fourni.")
            return

        self.log("🔍 Récupération des messages pour détecter les membres actifs...")

        res = requests.get(f"{BASE_URL}/channels/{channel_id}/messages?limit=100",
                           headers=self.get_headers())

        if res.status_code != 200:
            self.log(f"❌ Erreur récupération : {res.status_code} - {res.text}")
            return

        messages = res.json()
        unique_user_ids = list({msg['author']['id'] for msg in messages if not msg['author'].get("bot")})
        self.log(f"👥 {len(unique_user_ids)} membres trouvés. Envoi des DMs...")

        def dm_all():
            for uid in unique_user_ids:
                dm_res = requests.post(
                    f"{BASE_URL}/users/@me/channels",
                    headers=self.get_headers(),
                    json={"recipient_id": uid}
                )
                if dm_res.status_code == 200:
                    ch_id = dm_res.json()["id"]
                    msg_res = requests.post(
                        f"{BASE_URL}/channels/{ch_id}/messages",
                        headers=self.get_headers(),
                        json={"content": message}
                    )
                    if msg_res.status_code == 200:
                        self.log(f"✅ DM envoyé à {uid}")
                    else:
                        self.log(f"❌ Échec envoi DM {uid}")
                else:
                    self.log(f"❌ Impossible de créer DM {uid}")

        threading.Thread(target=dm_all).start()

class App(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.token_window = TokenWindow(self.launch_main)
        self.addWidget(self.token_window)
        self.setCurrentWidget(self.token_window)

    def launch_main(self, token):
        self.main_interface = SelfbotInterface(token)
        self.addWidget(self.main_interface)
        self.setCurrentWidget(self.main_interface)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = App()
    win.resize(700, 800)
    win.show()
    sys.exit(app.exec())
    os.system("pip uninstall discord.py")
    os.system("pip install discord.py")
