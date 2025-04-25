from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from screens.account_management_screen import AccountManagementScreen
from screens.register_screen import RegisterScreen
from screens.sign_in_screen import SignInScreen
from utils.database import initialize_database, validate_user_credentials, add_test_data

class BankApp(App):
    def build(self):
        # Initialize the database and add test data
        initialize_database()
        add_test_data()

        # Create the ScreenManager and add screens
        sm = ScreenManager()
        sm.add_widget(SignInScreen(name='sign_in'))
        sm.add_widget(RegisterScreen(name='register'))
        sm.add_widget(AccountManagementScreen(name='account_management'))
        return sm

    def sign_in(self, username, pin):
        account_id = validate_user_credentials(username, pin)
        if account_id:
            # Pass the account_id to the account management screen
            account_management_screen = self.root.get_screen('account_management')
            account_management_screen.account_id = account_id
            self.root.current = 'account_management'
        else:
            self.show_popup("Error", "Invalid username or PIN.")

    def register(self):
        self.root.current = 'register'

    def show_popup(self, title, message):
        from kivy.uix.popup import Popup
        from kivy.uix.label import Label
        from kivy.uix.button import Button
        from kivy.uix.boxlayout import BoxLayout

        # Create a layout for the popup
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        label = Label(text=message)
        button = Button(text="OK", size_hint=(None, None), size=(100, 40))
        
        # Close the popup when the button is pressed
        def close_popup(instance):
            popup.dismiss()

        button.bind(on_press=close_popup)
        layout.add_widget(label)
        layout.add_widget(button)

        # Create and open the popup
        popup = Popup(title=title, content=layout, size_hint=(None, None), size=(400, 200))
        popup.open()

if __name__ == "__main__":
    BankApp().run()