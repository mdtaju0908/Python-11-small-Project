import st as st

st.title("🌐 Simple Web App")

# Sidebar Navigation
page = st.sidebar.radio("Go to", ["Home", "About"])

# ------------------ HOME ------------------
if page == "Home":
    st.header("🏠 Home Page")
    st.write("I am Home Page")
    st.write("I am running in UI app")

# ------------------ ABOUT ------------------
elif page == "About":
    st.header("ℹ️ About Page")
    st.write("Welcome to My Website")
    st.write("This is a simple HTML page.")

    if st.button("Click Me"):
        st.success("God")