# 🏦 ATM System Using Python & Streamlit

## 📌 About the Project

The **ATM System** is a simple, interactive web application developed using Python, Object-Oriented Programming (OOP), and Streamlit. It simulates basic ATM operations, allowing users to generate a PIN, deposit money, withdraw money, and check their account balance through a user-friendly interface.

This project demonstrates the practical implementation of Python classes, methods, conditional statements, and session state management using Streamlit.

## ✨ Features

* 🔐 **PIN Generation:** Generate a PIN to access ATM operations.
* 💰 **Deposit Money:** Deposit money into the account after PIN verification.
* 💸 **Withdraw Money:** Withdraw money if the PIN is correct and sufficient balance is available.
* 🏦 **Check Balance:** View the current account balance after PIN verification.
* 🖥️ **Interactive Interface:** Simple and user-friendly interface built with Streamlit.
* 🧩 **OOP Implementation:** Uses a Python class and methods to organize ATM operations.
* 🔄 **Session State Management:** Maintains the PIN and balance across Streamlit reruns during the session.

## 🛠️ Technologies Used

* **Python** — Core programming language
* **Streamlit** — Web application interface
* **Object-Oriented Programming (OOP)** — Class-based code organization
* **Streamlit Session State** — Stores the PIN and balance during the session

## 📂 Project Structure

```text
ATM-System/
│
├── app.py
├── requirements.txt
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone YOUR_REPOSITORY_URL
```

Replace `YOUR_REPOSITORY_URL` with your GitHub repository URL.

### 2. Navigate to the Project Folder

```bash
cd ATM-System
```

### 3. Install Dependencies

Make sure Python is installed on your system.

Install Streamlit using:

```bash
pip install streamlit
```

Alternatively, if you have a `requirements.txt` file, run:

```bash
pip install -r requirements.txt
```

### 4. Run the Application

Execute the following command in your terminal:

```bash
streamlit run app.py
```

The application will open in your browser. If it does not open automatically, visit the local URL displayed in your terminal.

## 🚀 How to Use

1. Run the application.
2. Select **Pin Generation** from the sidebar.
3. Enter a four-digit PIN and click **Generate PIN**.
4. Select **Deposit** to add money to your account.
5. Enter your PIN and the amount to deposit.
6. Select **Withdraw** to withdraw money after PIN verification.
7. Select **Check Balance** to view your current balance.

**Note:** The account balance starts at ₹0, and you must deposit money before making a withdrawal.

## 🧠 Concepts Implemented

### 1. Object-Oriented Programming

The `Atm` class groups related operations into separate methods, making the code easier to organize and maintain.

### 2. Constructor (`__init__`)

The constructor initializes the PIN and account balance in Streamlit's session state when they do not already exist.

### 3. Conditional Statements

`if`, `elif`, and `else` statements validate PINs, check available balances, and control ATM operations.

### 4. Session State

`st.session_state` stores the PIN and balance across Streamlit reruns within the same browser session.

### 5. User Input and Validation

Streamlit widgets such as `st.text_input()`, `st.number_input()`, and `st.button()` collect user input and trigger ATM operations.

## ⚠️ Limitations

* The PIN and balance are stored only in Streamlit session state and are not saved in a database.
* The application does not provide real banking or financial transactions.
* The PIN is not securely hashed or stored in a persistent authentication system.
* The current implementation does not enforce exactly four numeric digits during PIN generation.
* Deposit and withdrawal amounts can be zero because the minimum amount is set to `0`.
* The application does not include user registration, transaction history, or account management.

**Security Notice:** This project is intended for learning and demonstration purposes only. It should not be used for real financial transactions.

## 🔮 Future Improvements

* Add PIN validation to enforce exactly four digits.
* Integrate a database such as SQLite or MySQL.
* Add transaction history.
* Support multiple user accounts.
* Improve the interface with custom styling.
* Add secure authentication and persistent account management.

## 👨‍💻 Author

**Priyanshu Patidar**

Python | Object-Oriented Programming | Streamlit

---

⭐ If you find this project useful, consider giving the repository a star!
