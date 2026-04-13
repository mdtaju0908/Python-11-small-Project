import st as st

st.title("🔄 Unit Converter")

# Category selection
category = st.selectbox("Select Category", ["Length", "Weight", "Temperature"])

value = st.number_input("Enter Value", value=0.0)

# ------------------ LENGTH ------------------
if category == "Length":
    option = st.selectbox(
        "Choose Conversion",
        ["Meter → Kilometer", "Kilometer → Meter", "Centimeter → Meter"]
    )

    if st.button("Convert"):
        if option == "Meter → Kilometer":
            result = value / 1000
            st.success(f"{result} Kilometer")

        elif option == "Kilometer → Meter":
            result = value * 1000
            st.success(f"{result} Meter")

        elif option == "Centimeter → Meter":
            result = value / 100
            st.success(f"{result} Meter")

# ------------------ WEIGHT ------------------
elif category == "Weight":
    option = st.selectbox(
        "Choose Conversion",
        ["Gram → Kilogram", "Kilogram → Gram", "Tonne → Kilogram"]
    )

    if st.button("Convert"):
        if option == "Gram → Kilogram":
            result = value / 1000
            st.success(f"{result} Kilogram")

        elif option == "Kilogram → Gram":
            result = value * 1000
            st.success(f"{result} Gram")

        elif option == "Tonne → Kilogram":
            result = value * 1000
            st.success(f"{result} Kilogram")

# ------------------ TEMPERATURE ------------------
elif category == "Temperature":
    option = st.selectbox(
        "Choose Conversion",
        ["Celsius → Fahrenheit", "Fahrenheit → Celsius"]
    )

    if st.button("Convert"):
        if option == "Celsius → Fahrenheit":
            result = (value * 9/5) + 32
            st.success(f"{result} °F")

        elif option == "Fahrenheit → Celsius":
            result = (value - 32) * 5/9
            st.success(f"{result} °C")