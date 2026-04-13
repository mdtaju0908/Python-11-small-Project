import streamlit as st
import os

st.title("📁 File Transfer App")

UPLOAD_FOLDER = "uploads"

# Create folder if not exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# ------------------ Upload Section ------------------
st.header("📤 Upload File")

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    st.success(f"✅ {uploaded_file.name} uploaded successfully!")

# ------------------ File List ------------------
st.header("📥 Download Files")

files = os.listdir(UPLOAD_FOLDER)

if files:
    for file in files:
        file_path = os.path.join(UPLOAD_FOLDER, file)

        with open(file_path, "rb") as f:
            st.download_button(
                label=f"Download {file}",
                data=f,
                file_name=file
            )
else:
    st.info("No files uploaded yet")