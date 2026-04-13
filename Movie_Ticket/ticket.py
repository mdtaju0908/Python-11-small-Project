import st as st

st.title("🎬 Movie Ticket Checker")

# Input
age = st.number_input("Enter Your Age", min_value=0, step=1)

ticket = st.checkbox("Do you have a ticket?")

# Button
if st.button("Check Eligibility"):

    if age > 18:
        st.success("✅ You can watch the movie")

        if ticket:
            st.success("🎟️ You can go inside")
        else:
            st.warning("⚠️ You need a ticket")

    elif age < 15:
        st.info("👨‍👩‍👧 You can watch the movie with parents")

    else:
        st.error("❌ Not allowed")