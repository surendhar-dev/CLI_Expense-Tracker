# tracker/cli.py
def display_menu():
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Search by Category")
    print("4. Total Spending")
    print("5. Delete Expense")
    print("6. Exit")

def print_table(expenses: list):
    """Formats a clean console table for viewing expenses."""
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\nID  | Amount   | Category   | Description")
    print("-" * 45)
    for e in expenses:
        print(f"{e['id']:<3} | ₹{e['amount']:<7.2f} | {e['category']:<10} | {e['description']}")