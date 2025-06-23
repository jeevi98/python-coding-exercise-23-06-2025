import json
import os
from datetime import datetime

DATA_FILE = "budget_data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {"income": 0.0, "expenses": []}

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def add_income(data):
    try:
        amount = float(input("Enter income amount (₹): "))
        data["income"] += amount
        print(f" Income of ₹{amount} added.")
    except ValueError:
        print(" Invalid amount.")

def add_expense(data):
    try:
        category = input("Enter category (e.g., Food, Rent, Travel): ")
        amount = float(input("Enter expense amount (₹): "))
        date = datetime.now().strftime("%Y-%m-%d")
        data["expenses"].append({"category": category, "amount": amount, "date": date})
        print(f" Expense of ₹{amount} for '{category}' added.")
    except ValueError:
        print(" Invalid amount.")

def show_summary(data):
    total_expenses = sum(exp["amount"] for exp in data["expenses"])
    balance = data["income"] - total_expenses

    print("\n Monthly Summary")
    print("-" * 30)
    print(f"Total Income: ₹{data['income']:.2f}")
    print(f"Total Expenses: ₹{total_expenses:.2f}")
    print(f"Balance: ₹{balance:.2f}")

    print("\n Expenses by Category:")
    category_totals = {}
    for exp in data["expenses"]:
        category = exp["category"]
        category_totals[category] = category_totals.get(category, 0) + exp["amount"]
    for cat, amt in category_totals.items():
        print(f"  {cat}: ₹{amt:.2f}")

def main():
    data = load_data()
    while True:
        print("\n Budget Tracker CLI")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Show Summary")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_income(data)
        elif choice == '2':
            add_expense(data)
        elif choice == '3':
            show_summary(data)
        elif choice == '4':
            save_data(data)
            print(" Data saved. Goodbye!")
            break
        else:
            print(" Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
