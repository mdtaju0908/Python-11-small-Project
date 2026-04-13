import streamlit as st

# Session state initialize
if "balance" not in st.session_state:
    st.session_state.balance = 12000

if "pin_verified" not in st.session_state:
    st.session_state.pin_verified = False

if "attempts" not in st.session_state:
    st.session_state.attempts = 0

PIN = 2121
MAX_ATTEMPTS = 3

st.title("🏧 ATM Pin System")

# PIN Verification
if not st.session_state.pin_verified:
    st.subheader("Enter your 4-digit PIN")

    user_pin = st.text_input("PIN", type="password")

    if st.button("Verify PIN"):
        if st.session_state.attempts >= MAX_ATTEMPTS:
            st.error("🚫 Card Blocked! Too many attempts.")
        else:
            if user_pin.isdigit() and int(user_pin) == PIN:
                st.session_state.pin_verified = True
                st.success("✅ PIN Verified Successfully!")
            else:
                st.session_state.attempts += 1
                remaining = MAX_ATTEMPTS - st.session_state.attempts
                st.error(f"❌ Invalid PIN! Attempts left: {remaining}")

# Main Menu
else:
    st.sidebar.title("Menu")
    option = st.sidebar.radio(
        "Select Option",
        ["Check Balance", "Withdraw Money", "Deposit Money", "Exit"]
    )

    if option == "Check Balance":
        st.subheader("💰 Your Balance")
        st.success(f"₹ {st.session_state.balance}")

    elif option == "Withdraw Money":
        st.subheader("💸 Withdraw Money")
        amount = st.number_input("Enter amount", min_value=1)

        if st.button("Withdraw"):
            if amount > st.session_state.balance:
                st.error("❌ Insufficient Balance!")
            else:
                st.session_state.balance -= amount
                st.success(f"₹ {amount} withdrawn successfully!")
                st.info(f"New Balance: ₹ {st.session_state.balance}")

    elif option == "Deposit Money":
        st.subheader("💵 Deposit Money")
        amount = st.number_input("Enter amount", min_value=1)

        if st.button("Deposit"):
            st.session_state.balance += amount
            st.success(f"₹ {amount} deposited successfully!")
            st.info(f"New Balance: ₹ {st.session_state.balance}")

    elif option == "Exit":
        st.warning("👋 Thank you for using ATM!")
        st.session_state.pin_verified = False