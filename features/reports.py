"""Reporting helpers for BudgetBuddy.

Heads up: this module is half-built on purpose. `account_summary` works, but
`category_report` is still a stub with a clear seam to finish (see the tickets).
"""


def account_summary(data):
    return data["account_name"] + ": " + str(len(data["transactions"])) + " transactions"


def category_report(data):
    """Total up the amount spent or earned in each category.

    Returns a dict like {"food": -12.5, "income": 20.0}. An account with no
    transactions returns an empty dict.
    """
    report = {}
    for t in data.get("transactions", []):
        name = t["category"]
        report[name] = round(report.get(name, 0) + t["amount"], 2)
    return report
