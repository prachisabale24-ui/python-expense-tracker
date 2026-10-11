
import os

FILE_NAME = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "expenses.txt"
)

expenses = []

# Load saved expenses
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r") as file:
        for line in file:
            try:
                name, amount = line.strip().rsplit("|", 1)
                expenses.append((name, float(amount)))
            except ValueError:
                continue

while True:
    print("\n--- My Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total Spending")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        name = input("Enter expense name: ").strip()

        if not name or "|" in name:
            print("Please enter a valid expense name!")
            continue

        try:
            amount = float(input("Enter amount in ₹: "))

            if amount <= 0:
                print("Amount must be greater than zero!")
                continue

            expenses.append((name, amount))

            with open(FILE_NAME, "a") as file:
                file.write(f"{name}|{amount}\n")

            print("Expense added and saved successfully!")

        except ValueError:
            print("Invalid amount! Please enter numbers only.")

    elif choice == "2":
        if not expenses:
            print("No expenses added yet.")
        else:
            print("\n--- Your Expenses ---")
            for name, amount in expenses:
                print(f"{name} - ₹{amount:.2f}")

    elif choice == "3":
        total = sum(amount for name, amount in expenses)
        print(f"Total Spending: ₹{total:.2f}")

    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice! Please select 1-4.")
