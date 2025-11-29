#Streamlit Dashboard
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Streamlit app of VGU")
st.text("Welcome to Md_Taju Dashboard")
st.header("Welcome")
st.write("You can write:", 10 + 5)

name = st.text_input("Enter your name:")
age = st.number_input("Enter the age")

st.write("Your name is:", name)

st.selectbox("Enter your course:", ["BA", "BTECH", "MTECH"])

if st.button("Click Me"):
    st.success("Button Clicked!")

file = st.file_uploader("Upload your file")
if file:
    content = file.read()
    st.write("File uploaded successfully!")

# Correct DataFrame
data = pd.DataFrame({
    "Name": ["TAJU", "ARIF", "MUNNA", "SHIVAM"],
    "Marks": [10, 20, 20, 10]
})

# Display dataframe
st.write("Student Data:")
st.dataframe(data)

# Correct chart data
marks_df = pd.DataFrame({
    "Marks": [10, 20, 20, 10]
})

# Correct chart functions
st.line_chart(marks_df)
st.bar_chart(marks_df)