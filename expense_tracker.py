import json
import time

# Terminal colors
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

FILE_NAME = "expenses.json"

# Load previously saved expenses if the file already exists
try:
    with open(FILE_NAME, "r") as file:
        expenses = json.load(file)
except FileNotFoundError:
    expenses = []

print("\n==========================================")
print(CYAN + "   💰 PERSONAL EXPENSE TRACKER 💰" + RESET)
print("==========================================")

while True:
    print("\nWhat would you like to do?")
    print("1. ➕ Add a new expense")
    print("2. 📋 View all expenses & total")
    print("3. 🚪 Exit")

    choice = input("\nChoose an option (1-3): ").strip()

    if choice == "1":
        item = input("🛒 What did you spend money on? ").strip()
        category = input("🏷️  Category (e.g., Food, Transport, Bills): ").strip()

        # float() converts typed text into a decimal number (like 12.50)
        try:
            amount = float(input("💵 Amount spent: "))
        except ValueError:
            print(RED + "❌ Please enter a valid number for the amount." + RESET)
            continue

        # Bundle details into a dictionary and add to the list
        expense = {
            "item": item,
            "category": category,
            "amount": amount
        }
        expenses.append(expense)

        # Save the updated list to expenses.json right away
        with open(FILE_NAME, "w") as file:
            json.dump(expenses, file, indent=4)

        print(GREEN + f"✅ Saved: {item} [{category}] - ${amount:.2f}" + RESET)

    elif choice == "2":
        print("\n------------------------------------------")
        print(YELLOW + "📊 YOUR EXPENSE SUMMARY" + RESET)
        print("------------------------------------------")

        if len(expenses) == 0:
            print("No expenses recorded yet. Choose option 1 to add one!")
        else:
            total = 0
            for exp in expenses:
                print(f"• {exp['item']} [{exp['category']}] — ${exp['amount']:.2f}")
                total = total + exp["amount"]

            print("------------------------------------------")
            print(GREEN + f"💰 Total Spent: ${total:.2f}" + RESET)

        print("------------------------------------------")

    elif choice == "3":
        print(CYAN + "\n💾 All expenses saved to expenses.json. Goodbye! 👋\n" + RESET)
        time.sleep(0.5)
        break

    else:
        print(RED + "❌ Invalid choice. Please enter 1, 2, or 3." + RESET)