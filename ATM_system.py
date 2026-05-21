import streamlit as st

class Atm:

    def __init__(self):
        if "pin" not in st.session_state:
            st.session_state.pin = None

        if "balance" not in st.session_state:
            st.session_state.balance = 0

    def pin_generation(self):
        pin = st.text_input("Enter your 4 digit PIN", type="password")

        if st.button("Generate PIN"):
            st.session_state.pin = pin
            st.success("PIN generated successfully")

    def deposit(self):
        pin = st.text_input("Enter your PIN", type="password")
        amount = st.number_input("Enter amount to deposit", min_value=0)

        if st.button("Deposit"):
            if st.session_state.pin == pin:
                st.session_state.balance += amount
                st.success("Amount deposited successfully")
            else:
                st.error("Invalid PIN")

    def withdraw(self):
        pin = st.text_input("Enter your PIN", type="password")
        amount = st.number_input("Enter amount to withdraw", min_value=0)

        if st.button("Withdraw"):
            if st.session_state.pin == pin:

                if amount <= st.session_state.balance:
                    st.session_state.balance -= amount
                    st.success("Withdrawal successful")

                else:
                    st.error("Insufficient balance")

            else:
                st.error("Invalid PIN")

    def display(self):
        pin = st.text_input("Enter your PIN", type="password")

        if st.button("Check Balance"):
            if st.session_state.pin == pin:
                st.info(f"Your current balance is ₹{st.session_state.balance}")
            else:
                st.error("Invalid PIN")


st.title("🏦 ATM System")

atm = Atm()

option = st.sidebar.selectbox(
    "Choose Option",
    ["Pin Generation", "Deposit", "Withdraw", "Check Balance"]
)

if option == "Pin Generation":
    atm.pin_generation()

elif option == "Deposit":
    atm.deposit()

elif option == "Withdraw":
    atm.withdraw()

elif option == "Check Balance":
    atm.display()