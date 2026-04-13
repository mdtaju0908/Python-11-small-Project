import st as st
import pyttsx3
import os

st.title("🎤 Text to Speech App")

# Init engine (once)
if "engine" not in st.session_state:
    st.session_state.engine = pyttsx3.init()

engine = st.session_state.engine

# Input text
text = st.text_area("Enter text to speak")

# Speak button
if st.button("🔊 Speak"):
    if text:
        engine.say(text)
        engine.runAndWait()
        st.success("✅ Speaking...")
    else:
        st.warning("⚠️ Enter some text")

# ------------------ Command Section ------------------
st.header("🧠 Command Executor")

command = st.text_input("Enter command (e.g. open notepad)")

if st.button("Run Command"):
    if "notepad" in command.lower():
        st.info("Opening Notepad...")
        os.system("notepad")
    else:
        st.error("❌ Unknown command")