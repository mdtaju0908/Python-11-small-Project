import streamlit as st

st.set_page_config(page_title="Calculator App", layout="centered")

st.title("🧮 Smart Calculator (Streamlit)")

# Tabs for features
tab1, tab2 = st.tabs(["Basic Calculator", "Conversions"])

# ------------------ BASIC CALCULATOR ------------------
with tab1:
    st.subheader("➕ Basic Operations")

    a = st.number_input("Enter first number", value=0.0)
    b = st.number_input("Enter second number", value=0.0)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Add"):
            st.success(f"Sum = {a + b}")

        if st.button("Subtract"):
            st.success(f"Subtraction = {a - b}")

    with col2:
        if st.button("Multiply"):
            st.success(f"Multiplication = {a * b}")

        if st.button("Divide"):
            if b != 0:
                st.success(f"Division = {a / b}")
            else:
                st.error("❌ Cannot divide by zero")

# ------------------ CONVERSIONS ------------------
with tab2:
    st.subheader("🔄 Unit Conversions")

    option = st.selectbox(
        "Choose Conversion",
        ["Celsius to Fahrenheit", "KM to Meter", "KG to Pounds"]
    )

    value = st.number_input("Enter value", value=0.0)

    if option == "Celsius to Fahrenheit":
        result = value * (9/5) + 32
        st.success(f"🌡️ Fahrenheit = {result}")

    elif option == "KM to Meter":
        result = value * 1000
        st.success(f"📏 Meters = {result}")

    elif option == "KG to Pounds":
        result = value * 2.20462
        st.success(f"⚖️ Pounds = {result}")