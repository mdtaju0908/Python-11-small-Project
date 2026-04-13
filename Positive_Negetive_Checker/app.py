import st as st

st.title("🔢 Number Checker")

# Input
num = st.number_input("Enter a number", value=0)

# Button
if st.button("Check"):
    if num > 0:
        st.success("✅ Positive Number")
    elif num < 0:
        st.error("❌ Negative Number")
    else:
        st.info("⚪ Zero")