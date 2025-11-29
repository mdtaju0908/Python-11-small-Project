"""
ATM PIN System - A simple ATM PIN verification system
"""


class ATMPinSystem:
    """ATM PIN System for managing user PIN verification."""

    def __init__(self):
        """Initialize the ATM system with default PIN."""
        self._pin = "1234"  # Default PIN
        self._balance = 1000.0
        self._max_attempts = 3

    def verify_pin(self, pin):
        """Verify if the entered PIN is correct."""
        return pin == self._pin

    def change_pin(self, old_pin, new_pin):
        """Change the PIN if old PIN is correct."""
        if self.verify_pin(old_pin):
            if len(new_pin) == 4 and new_pin.isdigit():
                self._pin = new_pin
                return True, "PIN changed successfully!"
            return False, "PIN must be exactly 4 digits."
        return False, "Incorrect old PIN."

    def check_balance(self, pin):
        """Check account balance."""
        if self.verify_pin(pin):
            return True, f"Your balance is: ${self._balance:.2f}"
        return False, "Incorrect PIN."

    def withdraw(self, pin, amount):
        """Withdraw money from account."""
        if not self.verify_pin(pin):
            return False, "Incorrect PIN."
        if amount <= 0:
            return False, "Invalid amount."
        if amount > self._balance:
            return False, "Insufficient funds."
        self._balance -= amount
        return True, f"Withdrawn: ${amount:.2f}. New balance: ${self._balance:.2f}"

    def deposit(self, pin, amount):
        """Deposit money to account."""
        if not self.verify_pin(pin):
            return False, "Incorrect PIN."
        if amount <= 0:
            return False, "Invalid amount."
        self._balance += amount
        return True, f"Deposited: ${amount:.2f}. New balance: ${self._balance:.2f}"


def main():
    """Main function to run the ATM system."""
    atm = ATMPinSystem()
    attempts = 0

    print("=" * 40)
    print("       Welcome to ATM PIN System")
    print("=" * 40)

    while attempts < 3:
        pin = input("\nEnter your PIN: ")
        if atm.verify_pin(pin):
            print("\nPIN verified successfully!")
            break
        else:
            attempts += 1
            remaining = 3 - attempts
            if remaining > 0:
                print(f"Incorrect PIN. {remaining} attempts remaining.")
            else:
                print("Too many incorrect attempts. Card blocked.")
                return

    while True:
        print("\n" + "-" * 40)
        print("1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Change PIN")
        print("5. Exit")
        print("-" * 40)

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            success, message = atm.check_balance(pin)
            print(message)

        elif choice == "2":
            try:
                amount = float(input("Enter amount to withdraw: $"))
                success, message = atm.withdraw(pin, amount)
                print(message)
            except ValueError:
                print("Invalid amount entered.")

        elif choice == "3":
            try:
                amount = float(input("Enter amount to deposit: $"))
                success, message = atm.deposit(pin, amount)
                print(message)
            except ValueError:
                print("Invalid amount entered.")

        elif choice == "4":
            old_pin = input("Enter current PIN: ")
            new_pin = input("Enter new PIN (4 digits): ")
            success, message = atm.change_pin(old_pin, new_pin)
            print(message)
            if success:
                pin = new_pin

        elif choice == "5":
            print("\nThank you for using ATM PIN System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
