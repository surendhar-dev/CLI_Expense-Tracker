import tracker

def show_menu():
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Search by Category")
    print("4. Total Spending")
    print("5. Delete Expense")
    print("6. Exit")

def run():
    while True:
        show_menu()
        choice = input("Choose: ").strip()

        if choice == "1":
            try:
                # Remove currency symbols like ₹ if entered by mistake
                raw_amt = input("Amount: ").replace("₹", "").strip()
                amount = float(raw_amt)
                category = input("Category: ").strip()
                description = input("Description: ").strip()
                
                tracker.add_expense(amount, category, description)
                print(" Expense added successfully!")
            except ValueError:
                print(" Invalid amount. Please enter a valid number.")

        elif choice == "2":
            expenses = tracker.get_all_expenses()
            if not expenses:
                print("No expenses recorded yet.")
            else:
                print("\nID | Amount   | Category   | Description")
                print("-" * 40)
                for e in expenses:
                    print(f"{e['id']}  | ₹{e['amount']:<8.2f} | {e['category']:<10} | {e['description']}")

        elif choice == "3":
            cat = input("Category to search: ").strip()
            matches = tracker.filter_by_category(cat)
            if not matches:
                print(f"No expenses found in category '{cat}'.")
            else:
                for e in matches:
                    print(f"ID {e['id']}: ₹{e['amount']} - {e['description']}")

        elif choice == "4":
            total = tracker.calculate_total()
            print(f"\nTotal Spending: ₹{total:.2f}")

        elif choice == "5":
            try:
                exp_id = int(input("Expense ID to delete: "))
                if tracker.delete_expense(exp_id):
                    print(" Expense deleted.")
                else:
                    print(" ID not found.")
            except ValueError:
                print(" Please enter a valid ID number.")

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid selection. Try again.")

if __name__ == "__main__":
    run()