def atm_system():
    balance = 12000
    pin = 2121
    attempts = 0
    max_attempts = 3

    print("--- Welcome to the ATM ---")

    while attempts < max_attempts:
        try:
            user_pin = int(input("\nEnter your 4-digit PIN: "))
        except ValueError:
            print("Invalid input! Please enter numbers only.")
            attempts += 1
            continue

        if user_pin == pin:
            print("\nPIN Verified Successfully!")
            
            while True:
                print("\n--- Main Menu ---")
                print("1. Check Balance")
                print("2. Withdraw Money")
                print("3. Deposit Money")
                print("4. Exit")
                
                try:
                    choice = int(input("Select an option (1-4): "))
                except ValueError:
                    print("Invalid input! Please select a number between 1 and 4.")
                    continue

                if choice == 1:
                    print(f"\nYour current balance is: ₹{balance}")
                
                elif choice == 2:
                    try:
                        amount = int(input("\nEnter the amount to withdraw: "))
                        if amount <= 0:
                            print("Amount must be greater than 0.")
                        elif amount > balance:
                            print("Insufficient balance!")
                        else:
                            balance -= amount
                            print(f"Transaction successful! ₹{amount} withdrawn.")
                            print(f"New balance: ₹{balance}")
                    except ValueError:
                        print("Invalid amount! Please enter a number.")
                
                elif choice == 3:
                    try:
                        amount = int(input("\nEnter the amount to deposit: "))
                        if amount <= 0:
                            print("Amount must be greater than 0.")
                        else:
                            balance += amount
                            print(f"₹{amount} deposited successfully!")
                            print(f"New balance: ₹{balance}")
                    except ValueError:
                        print("Invalid amount! Please enter a number.")
                
                elif choice == 4:
                    print("Thank you for using our ATM. Have a nice day!")
                    return
                
                else:
                    print("Invalid choice! Please select between 1 and 4.")
            
        else:
            attempts += 1
            remaining = max_attempts - attempts
            print(f"Invalid PIN! You have {remaining} attempts left.")

    print("\nAccess Denied! Your card is blocked for security reasons.")

if __name__ == "__main__":
    atm_system()
