from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from utils.database import get_account_balance, update_account_balance
from kivy.lang import Builder
Builder.load_file('kivy-banking-app/assets/styles/account_management_screen.kv')
class AccountManagementScreen(Screen):
    account_id = None  # This will be set when the user logs in

    def deposit(self):
        if not self.account_id:
            self.show_popup("Error", "No account ID found.")
            return

        # Create a popup to enter the deposit amount
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        input_field = TextInput(hint_text="Enter deposit amount", multiline=False, input_filter='float')
        submit_button = Button(text="Submit", size_hint=(None, None), size=(100, 40))
        cancel_button = Button(text="Cancel", size_hint=(None, None), size=(100, 40))

        popup = Popup(title="Deposit", content=layout, size_hint=(None, None), size=(400, 200))

        def submit_deposit(instance):
            try:
                amount = float(input_field.text)
                if amount <= 0:
                    self.show_popup("Error", "Deposit amount must be greater than zero.")
                else:
                    # Update the account balance in the database
                    update_account_balance(self.account_id, amount, "deposit")
                    self.show_popup("Success", f"Successfully deposited ${amount:.2f}.")
                    popup.dismiss()
            except ValueError:
                self.show_popup("Error", "Invalid amount entered.")

        submit_button.bind(on_press=submit_deposit)
        cancel_button.bind(on_press=popup.dismiss)

        layout.add_widget(input_field)
        layout.add_widget(submit_button)
        layout.add_widget(cancel_button)
        popup.open()

    def show_popup(self, title, message):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        label = Label(text=message, size_hint=(1, None), height=200)
        close_button = Button(text="Close", size_hint=(None, None), size=(100, 40))

        popup = Popup(title=title, content=layout, size_hint=(None, None), size=(400, 300))
        close_button.bind(on_press=popup.dismiss)

        layout.add_widget(label)
        layout.add_widget(close_button)
        popup.open()