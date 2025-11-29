# Unit Converter Program

def length_converter():
    print("\n📏 Length Converter")
    print("1. Meter to Kilometer")
    print("2. Kilometer to Meter")
    print("3. Centimeter to Meter")
    
    choice = int(input("Enter choice: "))
    value = float(input("Enter value: "))
    
    if choice == 1:
        print("Result:", value / 1000, "Kilometer")
    elif choice == 2:
        print("Result:", value * 1000, "Meter")
    elif choice == 3:
        print("Result:", value / 100, "Meter")
    else:
        print("Invalid choice!")


def weight_converter():
    print("\n⚖ Weight Converter")
    print("1. Gram to Kilogram")
    print("2. Kilogram to Gram")
    print("3. Tonne to Kilogram")
    
    choice = int(input("Enter choice: "))
    value = float(input("Enter value: "))
    
    if choice == 1:
        print("Result:", value / 1000, "Kilogram")
    elif choice == 2:
        print("Result:", value * 1000, "Gram")
    elif choice == 3:
        print("Result:", value * 1000, "Kilogram")
    else:
        print("Invalid choice!")


def temperature_converter():
    print("\n🌡 Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    
    choice = int(input("Enter choice: "))
    value = float(input("Enter value: "))
    
    if choice == 1:
        print("Result:", (value * 9/5) + 32, "°F")
    elif choice == 2:
        print("Result:", (value - 32) * 5/9, "°C")
    else:
        print("Invalid choice!")


# Main program
while True:
    print("\n===== UNIT CONVERTER =====")
    print("1. Length")
    print("2. Weight")
    print("3. Temperature")
    print("4. Exit")
    
    main_choice = int(input("Choose any option: "))
    
    if main_choice == 1:
        length_converter()
    elif main_choice == 2:
        weight_converter()
    elif main_choice == 3:
        temperature_converter()
    elif main_choice == 4:
        print("Thank you for using Unit Converter!")
        break
    else:
        print("Invalid input! Try again.")
