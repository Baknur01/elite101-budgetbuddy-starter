"""Tests for the category totals report (ticket 02)."""

import unittest

from features import reports


class TestCategoryReport(unittest.TestCase):
    def test_totals_each_category(self):
        data = {"account_name": "Sample", "starting_balance": 0, "transactions": [
            {"id": 1, "description": "Lunch", "amount": -8.25, "category": "food"},
            {"id": 2, "description": "Snack", "amount": -4.25, "category": "food"},
            {"id": 3, "description": "Allowance", "amount": 20.0, "category": "income"},
            {"id": 4, "description": "Bus pass", "amount": -2.5, "category": "transport"},
        ]}
        self.assertEqual(reports.category_report(data), {
            "food": -12.5,
            "income": 20.0,
            "transport": -2.5,
        })

    def test_every_transaction_counted_once(self):
        data = {"transactions": [
            {"id": 1, "description": "a", "amount": -1.0, "category": "fun"},
            {"id": 2, "description": "b", "amount": -2.0, "category": "fun"},
            {"id": 3, "description": "c", "amount": -3.0, "category": "fun"},
        ]}
        self.assertEqual(reports.category_report(data), {"fun": -6.0})

    def test_empty_account_returns_empty_dict(self):
        self.assertEqual(reports.category_report({"transactions": []}), {})


if __name__ == "__main__":
    unittest.main()
