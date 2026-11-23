# Python Personal Expense Tracker

A command-line application for recording daily expenses, viewing spending summaries, and saving records automatically to a local JSON file.

## Features
- **Add & Categorize Expenses:** Record item names, categories, and decimal amounts.
- **Automatic Persistence:** Saves all entries to `expenses.json` so data remains available across sessions.
- **Expense Summary & Total:** Loops through saved records to display every purchase and calculate total spending.
- **Input Validation:** Prevents crashes if non-numeric values are entered for an expense amount.

## How to Run
Make sure Python 3 is installed on your computer, then run:
```bash
python expense_tracker.py
```

## What I Learned
- Storing collections of data with Python **lists** and **dictionaries**
- Iterating through records and calculating totals with **`for` loops**
- Converting decimal inputs with **`float()`** and handling errors with **`try / except`**
- Reading and writing persistent data files using **`json`** and **`with open()`**
