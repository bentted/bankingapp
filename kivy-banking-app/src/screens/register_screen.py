from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from utils.database import create_account

Builder.load_file('assets/styles/main.kv')

class RegisterScreen(Screen):
    name_input = ObjectProperty(None)
    pin_input = ObjectProperty(None)

    def register(self):
        name = self.name_input.text
        pin = self.pin_input.text

        if not name or not pin:
            self.show_popup("Error", "Please fill in all fields.")
            return

        if len(pin) != 4 or not pin.isdigit():
            self.show_popup("Error", "PIN must be a 4-digit number.")
            return

        if create_account(name, pin):
            self.show_popup("Success", "Account created successfully!")
            self.name_input.text = ""
            self.pin_input.text = ""
        else:
            self.show_popup("Error", "An account with this name already exists.")

    def show_popup(self, title, message):
        popup = Popup(title=title, content=Label(text=message), size_hint=(None, None), size=(400, 200))
        popup.open()