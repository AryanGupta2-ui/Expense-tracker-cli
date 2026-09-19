"""
storage.py
Responsible for loading and saving expenses to a JSON file.
"""

import json
import os

DATA_FILE = os.path.join("data", "expenses.json")


def load_expenses():
    """
    Reads expenses from the JSON file.
    Returns an empty list if the file doesn't exist yet.
    """
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def save_expenses(expenses):
    """
    Writes the full list of expenses back to the JSON file.
    """
    os.makedirs("data", exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=4)


def get_next_id(expenses):
    """
    Figures out the next available ID by looking at existing expenses.
    """
    if not expenses:
        return 1
    return max(e["id"] for e in expenses) + 1