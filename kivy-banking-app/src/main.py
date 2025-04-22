from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from screens.register_screen import RegisterScreen
from screens.account_management_screen import AccountManagementScreen

class BankApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(RegisterScreen(name='register_screen'))
        sm.add_widget(AccountManagementScreen(name='account_management_screen'))
        return sm

if __name__ == "__main__":
    BankApp().run()