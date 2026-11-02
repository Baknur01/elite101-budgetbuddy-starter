"""Core BudgetBuddy logic: transactions, balance, and small helpers."""


def get_transactions(data):
    return data["transactions"]


def add_transaction(data, description, amount, category="general"):
    new_id = max((t["id"] for t in data["transactions"]), default=0) + 1
    tx = {"id": new_id, "description": description, "amount": amount, "category": category}
    data["transactions"].append(tx)
    return tx


def balance(data):
    return round(data["starting_balance"] + sum(t["amount"] for t in data["transactions"]), 2)


def list_transactions(transactions, show=print):
    for t in transactions:
        show(str(t["id"]) + ". " + t["description"] + " (" + str(t["amount"]) + ")")


def transactions_by_category(transactions, category):
    return [t for t in transactions if t["category"] == category]


def count_by_category(transactions):
    counts = {}
    for t in transactions:
        name = t["category"]
        counts[name] = counts.get(name, 0) + 1
    return counts


def last_transaction(transactions):
    return transactions[len(transactions) - 1]


def total_spent(transactions):
    return round(sum(-t["amount"] for t in transactions if t["amount"] < 0), 2)


def average_transaction(transactions):
    if not transactions:
        return 0
    return round(sum(t["amount"] for t in transactions) / len(transactions), 2)
def set_budget(data, category, amount):
    if "budgets" not in data:
        data["budgets"] = {}
    data["budgets"][category] = amount

def check_budget(data, category):
    if "budgets" not in data or category not in data["budgets"]:
        return None
    
    # Calculate total spending in this category
    spent = sum(t["amount"] for t in data["transactions"] if t.get("category") == category)
    limit = data["budgets"][category]
    return {"limit": limit, "spent": spent, "exceeded": spent > limit}