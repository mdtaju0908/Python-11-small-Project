"""
Calculator - A simple calculator with basic arithmetic operations
"""

import math


class Calculator:
    """A simple calculator class with basic operations."""

    def __init__(self):
        """Initialize calculator with history."""
        self.history = []

    def add(self, a, b):
        """Add two numbers."""
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result

    def subtract(self, a, b):
        """Subtract two numbers."""
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result

    def multiply(self, a, b):
        """Multiply two numbers."""
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result

    def divide(self, a, b):
        """Divide two numbers."""
        if b == 0:
            return "Error: Division by zero"
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result

    def power(self, base, exponent):
        """Calculate power of a number."""
        result = math.pow(base, exponent)
        self.history.append(f"{base} ^ {exponent} = {result}")
        return result

    def square_root(self, number):
        """Calculate square root."""
        if number < 0:
            return "Error: Cannot calculate square root of negative number"
        result = math.sqrt(number)
        self.history.append(f"√{number} = {result}")
        return result

    def modulo(self, a, b):
        """Calculate modulo of two numbers."""
        if b == 0:
            return "Error: Division by zero"
        result = a % b
        self.history.append(f"{a} % {b} = {result}")
        return result

    def clear_history(self):
        """Clear calculation history."""
        self.history = []
        return "History cleared."

    def show_history(self):
        """Show calculation history."""
        if not self.history:
            return "No calculations yet."
        return "\n".join(self.history)


def main():
    """Main function to run the calculator."""
    calc = Calculator()

    print("=" * 40)
    print("       Welcome to Calculator")
    print("=" * 40)

    while True:
        print("\n" + "-" * 40)
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power")
        print("6. Square Root")
        print("7. Modulo")
        print("8. Show History")
        print("9. Clear History")
        print("10. Exit")
        print("-" * 40)

        choice = input("Enter your choice (1-10): ")

        if choice in ["1", "2", "3", "4", "5", "7"]:
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))

                if choice == "1":
                    print(f"Result: {calc.add(a, b)}")
                elif choice == "2":
                    print(f"Result: {calc.subtract(a, b)}")
                elif choice == "3":
                    print(f"Result: {calc.multiply(a, b)}")
                elif choice == "4":
                    print(f"Result: {calc.divide(a, b)}")
                elif choice == "5":
                    print(f"Result: {calc.power(a, b)}")
                elif choice == "7":
                    print(f"Result: {calc.modulo(a, b)}")

            except ValueError:
                print("Invalid input. Please enter valid numbers.")

        elif choice == "6":
            try:
                num = float(input("Enter a number: "))
                print(f"Result: {calc.square_root(num)}")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        elif choice == "8":
            print("\nCalculation History:")
            print(calc.show_history())

        elif choice == "9":
            print(calc.clear_history())

        elif choice == "10":
            print("\nThank you for using Calculator. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
