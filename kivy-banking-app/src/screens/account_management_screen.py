from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from utils.database import deposit, withdrawal, check_balance, view_transactions

Builder.load_file('assets/styles/main.kv')

class AccountManagementScreen(Screen):
    account_id = ObjectProperty(None)

    def deposit(self):
        amount = self.get_amount_input("Deposit Amount")
        if amount is not None:
            if deposit(self.account_id, amount):
                self.show_popup("Success", "Deposit successful!")
            else:
                self.show_popup("Error", "Deposit failed.")

    def withdraw(self):
        amount = self.get_amount_input("Withdrawal Amount")
        if amount is not None:
            if withdrawal(self.account_id, amount):
                self.show_popup("Success", "Withdrawal successful!")
            else:
                self.show_popup("Error", "Insufficient funds or withdrawal failed.")

    def check_balance(self):
        balance = check_balance(self.account_id)
        if balance is not None:
            self.show_popup("Balance", f"Your current balance is: ${balance:.2f}")
        else:
            self.show_popup("Error", "Failed to retrieve balance.")

    def view_transactions(self):
        transactions = view_transactions(self.account_id)
        if transactions:
            transaction_log = "\n".join(
                [f"{t[2]} - {t[0].capitalize()}: ${t[1]:.2f}" for t in transactions]
            )
            self.show_popup("Transaction Log", transaction_log)
        else:
            self.show_popup("Transaction Log", "No transactions found.")

    def get_amount_input(self, title):
        try:
            amount = float(input(f"{title}: "))
            if amount > 0:
                return amount
            else:
                self.show_popup("Error", "Amount must be greater than 0.")
        except ValueError:
            self.show_popup("Error", "Invalid amount. Please enter a valid number.")
        return None

    def show_popup(self, title, message):
        popup = Popup(title=title, content=Label(text=message), size_hint=(None, None), size=(400, 200))
        popup.open()