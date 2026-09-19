"""
reports.py
Responsible for generating reports and summaries from expense data.
"""


def total_spent(expenses):
    """Returns the total amount spent across all expenses."""
    return sum(e["amount"] for e in expenses)


def total_by_category(expenses):
    """
    Returns a dictionary like {"Food": 500.0, "Travel": 200.0}
    showing total spent per category.
    """
    totals = {}
    for e in expenses:
        cat = e["category"]
        totals[cat] = totals.get(cat, 0) + e["amount"]
    return totals


def filter_by_category(expenses, category):
    """Returns only the expenses matching a given category."""
    return [e for e in expenses if e["category"].lower() == category.lower()]


def highest_expense(expenses):
    """Returns the single largest expense record, or None if empty."""
    if not expenses:
        return None
    return max(expenses, key=lambda e: e["amount"])


def print_summary_report(expenses):
    """Prints a full summary report to the console."""
    if not expenses:
        print("\nNo expenses to summarize yet.")
        return

    print("\n--- Summary Report ---")
    print(f"Total spent: ₹{total_spent(expenses):.2f}")

    print("\nBy category:")
    for cat, amt in total_by_category(expenses).items():
        print(f"  {cat}: ₹{amt:.2f}")

    top = highest_expense(expenses)
    print(f"\nHighest single expense: ₹{top['amount']:.2f} on {top['date']} ({top['category']} - {top['note']})")