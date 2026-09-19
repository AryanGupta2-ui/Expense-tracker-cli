"""
main.py
Entry point for the Expense Tracker CLI.
Shows a menu and connects expense.py and storage.py together.
"""

from expense import get_expense_input
from storage import load_expenses, save_expenses, get_next_id


def show_menu():
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Exit")


def view_expenses(expenses):
    if not expenses:
        print("\nNo expenses recorded yet.")
        return

    print("\n--- All Expenses ---")
    for e in expenses:
        print(f"ID {e['id']} | {e['date']} | {e['category']} | ₹{e['amount']} | {e['note']}")


def main():
    expenses = load_expenses()

    while True:
        show_menu()
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            next_id = get_next_id(expenses)
            new_expense = get_expense_input(next_id)
            if new_expense:
                expenses.append(new_expense)
                save_expenses(expenses)
                print("Expense added and saved successfully!")

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            print("Goodbye! Your data has been saved.")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()