import json
import os

DB_FILE = "data/expenses.json"

def load_data():
    """Reads JSON from disk into Python memory."""
    if not os.path.exists(DB_FILE):
        return {"next_id": 1, "expenses": []}

    with open(DB_FILE, "r") as file:
        return json.load(file)

def save_data(data):
    """Writes Python memory back to the JSON file."""
    os.makedirs(os.path.dirname(DB_FILE), exist_ok=True)
    
    with open(DB_FILE, "w") as file:
        json.dump(data, file, indent=2)