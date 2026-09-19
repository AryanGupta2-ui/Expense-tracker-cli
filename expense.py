"""
expense.py
Responsible for creating and validating a single expense record.
"""

from datetime import datetime


def create_expense(expense_id, date_str, category, amount, note=""):
    """
    Builds and validates one expense record.
    Returns a dictionary if valid, raises ValueError if not.
    """

    # --- validate date ---
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Date must be in YYYY-MM-DD format (e.g. 2026-09-19)")

    # --- validate amount ---
    try:
        amount = float(amount)
    except ValueError:
        raise ValueError("Amount must be a number (e.g. 250 or 250.50)")

    if amount <= 0:
        raise ValueError("Amount must be greater than 0")

    # --- validate category ---
    if not category.strip():
        raise ValueError("Category cannot be empty")

    expense = {
        "id": expense_id,
        "date": date_str,
        "category": category.strip().title(),
        "amount": amount,
        "note": note.strip()
    }

    return expense


def get_expense_input(next_id):
    """
    Prompts the user for expense details via the console.
    Returns a validated expense dict, or None if the user entered bad data.
    """
    print("\n--- Add New Expense ---")
    date_str = input("Date (YYYY-MM-DD), leave blank for today: ").strip()
    if date_str == "":
        date_str = datetime.now().strftime("%Y-%m-%d")

    category = input("Category (e.g. Food, Travel, Bills): ").strip()
    amount_str = input("Amount: ").strip()
    note = input("Note (optional): ").strip()

    try:
        expense = create_expense(next_id, date_str, category, amount_str, note)
        return expense
    except ValueError as e:
        print(f"Error: {e}")
        return None