from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from utils.database import validate_user_credentials

Builder.load_file('/home/kali/Desktop/projectpy/kivy-banking-app/assets/styles/sign_in_screen.kv')

class SignInScreen(Screen):
    def sign_in(self, username, pin):
        if validate_user_credentials(username, pin):
            self.manager.current = 'account_management'
        else:
            self.show_error_popup("Invalid credentials. Please try again.")

    def register(self):
        self.manager.current = 'register'

    def show_error_popup(self, message):
        from kivy.uix.popup import Popup
        from kivy.uix.label import Label
        popup = Popup(title='Error', content=Label(text=message), size_hint=(0.8, 0.4))
        popup.open()