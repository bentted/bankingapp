from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from utils.database import create_account

Builder.load_file('/home/kali/Desktop/projectpy/kivy-banking-app/assets/styles/register_screen.kv')

class RegisterScreen(Screen):
    def register(self, name, pin):
        if not name or not pin:
            self.show_popup("Error", "Please fill in all fields.")
            return

        if len(pin) != 4 or not pin.isdigit():
            self.show_popup("Error", "PIN must be a 4-digit number.")
            return

        account_id = create_account(name, pin)
        if account_id:
            self.show_popup("Success", f"Account created successfully! Your Account ID is: {account_id}")
        else:
            self.show_popup("Error", "An account with this name already exists.")

    def show_popup(self, title, message):
        from kivy.uix.popup import Popup
        from kivy.uix.label import Label
        popup = Popup(title=title, content=Label(text=message), size_hint=(None, None), size=(400, 200))
        popup.open()