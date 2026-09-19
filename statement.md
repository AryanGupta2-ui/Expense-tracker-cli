# Project Statement — Expense Tracker CLI

## Problem Statement

Most individuals track their daily spending inconsistently — using notebooks, scattered notes, or not at all — which makes it difficult to understand where their money actually goes each month. This project addresses that gap by providing a simple, lightweight command-line tool to record expenses and instantly generate spending summaries, without requiring a spreadsheet, an account, or an internet connection.

## Target Users

Any individual who wants to track personal expenses quickly from the command line, without the overhead of a full budgeting app or spreadsheet software.

## Scope

### In Scope
- Recording individual expenses with date, category, amount, and an optional note
- Persistent local storage of expense data (JSON file)
- Viewing all recorded expenses
- Generating a summary report: total spending, category-wise breakdown, and highest single expense
- Basic input validation (invalid dates, non-numeric amounts, empty categories are rejected with clear error messages)

### Out of Scope
- Multi-user support or login/authentication
- Cloud sync or online storage
- Graphical user interface (this is a command-line-only tool, by design)
- Editing or deleting existing expenses (potential future enhancement)
- Budget-setting and alerts (potential future enhancement)

## Functional Modules

1. **Data Entry Module** (`expense.py`) — Captures and validates expense details from the user.
2. **Storage Module** (`storage.py`) — Persists expense records to a JSON file and loads them back on startup.
3. **Reporting Module** (`reports.py`) — Aggregates and summarizes expense data (totals, category breakdowns, highest expense).
4. **Application Entry Point** (`main.py`) — Presents the menu-driven interface and coordinates the above modules.

## Technology Used

- **Language:** Python 3
- **Storage:** JSON file (no external database)
- **Interface:** Command-line (CLI), menu-driven
- **Libraries:** Python standard library only (`json`, `os`, `datetime`) — no external dependencies

## Expected Outcome

A fully functional, runnable-from-terminal expense tracker that lets a user log expenses across multiple sessions (data persists between runs) and view meaningful summaries of their spending habits.