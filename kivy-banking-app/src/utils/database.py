import sqlite3
import random
import string

def initialize_database():
    conn = sqlite3.connect("bank_system.db")
    cursor = conn.cursor()

    # Create the accounts table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS accounts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        account_id TEXT UNIQUE NOT NULL,
        name TEXT UNIQUE NOT NULL,
        pin TEXT NOT NULL,
        balance REAL DEFAULT 0.0
    )
    """)

    # Create the transactions table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        account_id TEXT NOT NULL,
        type TEXT NOT NULL,
        amount REAL NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (account_id) REFERENCES accounts (account_id)
    )
    """)

    conn.commit()
    conn.close()

def generate_account_id():
    conn = sqlite3.connect("bank_system.db")
    cursor = conn.cursor()

    while True:
        account_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        cursor.execute("SELECT 1 FROM accounts WHERE account_id = ?", (account_id,))
        if not cursor.fetchone():
            break

    conn.close()
    return account_id

def create_account(name, pin):
    conn = sqlite3.connect("bank_system.db")
    cursor = conn.cursor()

    account_id = generate_account_id()

    try:
        cursor.execute("INSERT INTO accounts (account_id, name, pin) VALUES (?, ?, ?)", 
                       (account_id, name, pin))
        conn.commit()
        return account_id
    except sqlite3.IntegrityError:
        return None
    finally:
        conn.close()

def validate_user_credentials(name, pin):
    conn = sqlite3.connect("bank_system.db")
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT account_id FROM accounts WHERE name = ? AND pin = ?", (name, pin))
        account = cursor.fetchone()
        return account[0] if account else None
    finally:
        conn.close()

def get_account_balance(account_id):
    conn = sqlite3.connect("bank_system.db")
    cursor = conn.cursor()

    cursor.execute("SELECT balance FROM accounts WHERE account_id = ?", (account_id,))
    result = cursor.fetchone()

    conn.close()
    return result[0] if result else 0.0

def add_test_data():
    """
    Adds test data to the database for development and testing purposes.
    """
    conn = sqlite3.connect("bank_system.db")
    cursor = conn.cursor()

    try:
        # Insert test account data
        cursor.execute("INSERT OR IGNORE INTO accounts (account_id, name, pin, balance) VALUES (?, ?, ?, ?)", 
                       ("TEST123456", "testuser", "1234", 100.0))

        # Insert test transactions for the test account
        cursor.execute("INSERT OR IGNORE INTO transactions (account_id, type, amount) VALUES (?, ?, ?)", 
                       ("TEST123456", "deposit", 50.0))
        cursor.execute("INSERT OR IGNORE INTO transactions (account_id, type, amount) VALUES (?, ?, ?)", 
                       ("TEST123456", "withdrawal", 20.0))

        conn.commit()
    finally:
        conn.close()

def update_account_balance(account_id, amount, transaction_type):
    """
    Updates the account balance and logs the transaction in the database.
    """
    conn = sqlite3.connect("bank_system.db")
    cursor = conn.cursor()

    try:
        # Update the account balance
        if transaction_type == "deposit":
            cursor.execute("UPDATE accounts SET balance = balance + ? WHERE account_id = ?", (amount, account_id))
        elif transaction_type == "withdrawal":
            cursor.execute("UPDATE accounts SET balance = balance - ? WHERE account_id = ?", (amount, account_id))

        # Log the transaction
        cursor.execute("INSERT INTO transactions (account_id, type, amount) VALUES (?, ?, ?)", 
                       (account_id, transaction_type, amount))

        conn.commit()
    finally:
        conn.close()