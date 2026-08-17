# CLI Expense Tracker

A lightweight command-line expense tracker built with Python and local JSON file storage.

## Project Structure

```text
expense_tracker/
│
├── tracker/
│   ├── __init__.py
│   ├── cli.py          # Command-line interface & argument parsing
│   ├── models.py       # Expense & Category data classes
│   ├── storage.py      # JSON file I/O operations
│   └── tracker.py      # Core business logic
│
├── data/
│   └── expenses.json   # Local JSON database file
│
├── main.py             # Main execution entry point
├── requirements.txt    # Optional dependencies
└── README.md           # Documentation
```

## Features

- Add expenses
- View all expenses
- Filter expenses by category
- Calculate total spending
- Delete expenses
- Automatically save expenses locally in JSON format

## How to Run

```bash
python main.py
```

## Storage

Expenses are stored locally in:

```text
data/expenses.json
```

No external database is required.
