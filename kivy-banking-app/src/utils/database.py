import sqlite3

def initialize_database():
    conn = sqlite3.connect("bank_system.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS accounts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            pin TEXT NOT NULL,
            balance REAL DEFAULT 0.0
        )
    """)

    conn.commit()
    conn.close()

def create_account(name, pin):
    conn = sqlite3.connect("bank_system.db")
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO accounts (name, pin) VALUES (?, ?)", (name, pin))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def validate_user(name, pin):
    conn = sqlite3.connect("bank_system.db")
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM accounts WHERE name = ? AND pin = ?", (name, pin))
    account = cursor.fetchone()

    conn.close()
    return account is not None

def get_account_balance(account_id):
    conn = sqlite3.connect("bank_system.db")
    cursor = conn.cursor()

    cursor.execute("SELECT balance FROM accounts WHERE id = ?", (account_id,))
    balance = cursor.fetchone()[0]

    conn.close()
    return balance

def get_all_accounts():
    conn = sqlite3.connect("bank_system.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM accounts")
    accounts = cursor.fetchall()

    conn.close()
    return accounts