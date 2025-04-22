from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.lang import Builder
from utils.database import validate_user_credentials

Builder.load_file('assets/styles/main.kv')

class SignInScreen(Screen):
    def __init__(self, **kwargs):
        super(SignInScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.username_input = TextInput(hint_text='Username', multiline=False)
        self.password_input = TextInput(hint_text='Password', password=True, multiline=False)

        self.sign_in_button = Button(text='Sign In')
        self.sign_in_button.bind(on_press=self.sign_in)

        self.layout.add_widget(Label(text='Sign In', font_size=32))
        self.layout.add_widget(self.username_input)
        self.layout.add_widget(self.password_input)
        self.layout.add_widget(self.sign_in_button)

        self.add_widget(self.layout)

    def sign_in(self, instance):
        username = self.username_input.text
        password = self.password_input.text

        if validate_user_credentials(username, password):
            self.manager.current = 'main'  # Transition to the main application screen
        else:
            self.show_error_popup("Invalid credentials. Please try again.")

    def show_error_popup(self, message):
        popup = Popup(title='Error', content=Label(text=message), size_hint=(0.8, 0.4))
        popup.open()