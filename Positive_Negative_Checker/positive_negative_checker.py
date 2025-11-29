"""
Positive Negative Checker - A simple number classifier
"""


class PositiveNegativeChecker:
    """Check if numbers are positive, negative, or zero."""

    def __init__(self):
        """Initialize the checker."""
        self.history = []

    def check_number(self, number):
        """Check if a number is positive, negative, or zero."""
        if number > 0:
            result = "Positive"
            emoji = "➕"
        elif number < 0:
            result = "Negative"
            emoji = "➖"
        else:
            result = "Zero"
            emoji = "0️⃣"

        self.history.append({
            "number": number,
            "result": result
        })

        return f"{emoji} {number} is {result}"

    def check_multiple(self, numbers):
        """Check multiple numbers at once."""
        results = []
        for num in numbers:
            results.append(self.check_number(num))
        return results

    def get_statistics(self):
        """Get statistics from checked numbers."""
        if not self.history:
            return "No numbers checked yet."

        positive_count = sum(
            1 for item in self.history if item["result"] == "Positive"
        )
        negative_count = sum(
            1 for item in self.history if item["result"] == "Negative"
        )
        zero_count = sum(
            1 for item in self.history if item["result"] == "Zero"
        )
        total = len(self.history)

        numbers = [item["number"] for item in self.history]
        avg = sum(numbers) / total if total > 0 else 0

        return f"""
📊 Statistics:
   Total numbers checked: {total}
   ➕ Positive: {positive_count} ({positive_count/total*100:.1f}%)
   ➖ Negative: {negative_count} ({negative_count/total*100:.1f}%)
   0️⃣  Zero: {zero_count} ({zero_count/total*100:.1f}%)
   📈 Maximum: {max(numbers)}
   📉 Minimum: {min(numbers)}
   📊 Average: {avg:.2f}
"""

    def get_history(self):
        """Get the check history."""
        if not self.history:
            return "No history yet."
        result = []
        for i, item in enumerate(self.history, 1):
            result.append(f"{i}. {item['number']} → {item['result']}")
        return "\n".join(result)

    def clear_history(self):
        """Clear the check history."""
        self.history = []
        return "History cleared."

    @staticmethod
    def is_positive(number):
        """Check if number is positive."""
        return number > 0

    @staticmethod
    def is_negative(number):
        """Check if number is negative."""
        return number < 0

    @staticmethod
    def is_zero(number):
        """Check if number is zero."""
        return number == 0

    @staticmethod
    def is_even(number):
        """Check if number is even."""
        return number % 2 == 0

    @staticmethod
    def is_odd(number):
        """Check if number is odd."""
        return number % 2 != 0


def main():
    """Main function to run the checker."""
    checker = PositiveNegativeChecker()

    print("=" * 50)
    print("     Welcome to Positive/Negative Checker")
    print("=" * 50)

    while True:
        print("\n" + "-" * 50)
        print("1. Check a single number")
        print("2. Check multiple numbers")
        print("3. View statistics")
        print("4. View history")
        print("5. Clear history")
        print("6. Additional checks (even/odd)")
        print("7. Exit")
        print("-" * 50)

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            try:
                number = float(input("Enter a number: "))
                print(f"\n{checker.check_number(number)}")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        elif choice == "2":
            try:
                input_str = input(
                    "Enter numbers separated by spaces or commas: "
                )
                # Handle both comma and space separated values
                input_str = input_str.replace(",", " ")
                numbers = [float(n) for n in input_str.split()]

                print("\nResults:")
                results = checker.check_multiple(numbers)
                for result in results:
                    print(f"  {result}")
            except ValueError:
                print("Invalid input. Please enter valid numbers.")

        elif choice == "3":
            print(checker.get_statistics())

        elif choice == "4":
            print("\n📜 History:")
            print(checker.get_history())

        elif choice == "5":
            print(checker.clear_history())

        elif choice == "6":
            try:
                number = float(input("Enter a number: "))
                print(f"\n{checker.check_number(number)}")

                # Additional checks for integers
                if number == int(number):
                    int_num = int(number)
                    even_odd = "Even" if checker.is_even(int_num) else "Odd"
                    print(f"   Also: This number is {even_odd}")
                else:
                    print("   (Even/Odd check only applies to integers)")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        elif choice == "7":
            print("\nThank you for using Positive/Negative Checker. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
