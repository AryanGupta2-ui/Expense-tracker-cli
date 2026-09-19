# Expense Tracker CLI

A simple command-line Python application to record personal expenses, save them persistently, and view spending summaries by category.

## Features

- **Add Expense** — record an expense with date, category, amount, and an optional note
- **View All Expenses** — list every recorded expense
- **View Summary Report** — see total spending, category-wise breakdown, and your highest single expense
- **Persistent Storage** — all data is saved to a local JSON file, so it survives between runs

## Project Structure

Expense-tracker-cli/
├── main.py # Entry point — runs the menu and connects everything
├── expense.py # Creates and validates a single expense record
├── storage.py # Loads and saves expenses to a JSON file
├── reports.py # Generates summary reports and category breakdowns
├── data/
│ └── expenses.json # Where your expense data is stored
├── README.md
└── statement.md # Problem statement and project scope


## Requirements

- Python 3.8 or later
- No external libraries required — uses only Python's built-in modules (`json`, `os`, `datetime`)

## Setup Instructions

1. **Clone this repository:**
```bash
   git clone https://github.com/AryanGupta2-ui/Expense-tracker-cli.git
   cd Expense-tracker-cli
```

2. **Verify Python is installed:**
```bash
   python --version
```
   You should see Python 3.8 or higher. If not, install it from [python.org](https://www.python.org/downloads/).

3. **No additional dependencies need to be installed** — the project only uses Python's standard library.

## How to Run

From the project's root folder, run:
```bash
python main.py
```

You'll see a menu:

===== Expense Tracker =====

Add Expense
View All Expenses
View Summary Report
Exit

Enter the number corresponding to your choice and follow the prompts.

### Example Usage

Choose an option (1-4): 1

--- Add New Expense ---
Date (YYYY-MM-DD), leave blank for today:
Category (e.g. Food, Travel, Bills): Food
Amount: 250
Note (optional): lunch
Expense added and saved successfully!


## Data Storage

All expenses are saved in `data/expenses.json` in the following format:
```json
{
    "id": 1,
    "date": "2026-09-19",
    "category": "Food",
    "amount": 250.0,
    "note": "lunch"
}
```

This file is created automatically the first time you add an expense — no manual setup needed.

## Author

Aryan Gupta — built this project for the VIT flipped course evaluation.