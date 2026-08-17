from tracker.storage import load_data, save_data

def add_expense(amount, category, description):
    data = load_data()
    
    new_expense = {
        "id": data["next_id"],
        "amount": amount,
        "category": category,
        "description": description
    }
    
    data["expenses"].append(new_expense)
    data["next_id"] += 1  # Increment ID so every expense has a unique key
    
    save_data(data)

def get_all_expenses():
    data = load_data()
    return data["expenses"]

def filter_by_category(category):
    data = load_data()
    return [e for e in data["expenses"] if e["category"].lower() == category.lower()]

def calculate_total():
    data = load_data()
    return sum(e["amount"] for e in data["expenses"])

def delete_expense(expense_id):
    data = load_data()
    initial_length = len(data["expenses"])
    data["expenses"] = [e for e in data["expenses"] if e["id"] != expense_id]
    
    if len(data["expenses"]) < initial_length:
        save_data(data)
        return True
    return False