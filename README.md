# Kivy Banking Application

This project is a comprehensive banking application developed using Kivy, a Python framework designed for building multitouch applications. It provides a user-friendly interface for managing banking accounts, including features such as user registration, sign-in, account management, and transaction history.

## Project Overview

The application is structured to ensure modularity and ease of maintenance. It includes separate modules for user interface design, business logic, and database management.

## Key Features

- **User Registration**: 
  - New users can securely create accounts by providing their details.
  - Passwords are securely stored to ensure user privacy.

- **User Sign-In**: 
  - Existing users can log in using their credentials to access their accounts.
  - Includes basic error handling for incorrect credentials.

- **Account Management**:
  - **Deposit**: Users can deposit money into their accounts.
  - **Withdrawal**: Users can withdraw money, with checks for sufficient balance.
  - **Check Balance**: Users can view their current account balance.
  - **Transaction Log**: A detailed log of all transactions (deposits, withdrawals) is available for users to review.

- **Transaction History**:
  - Displays a chronological list of all transactions, including timestamps and transaction types.

## Getting Started

Follow the steps below to set up and run the application:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd kivy-banking-app
pip install -r requirements.txt
python src/main.py
