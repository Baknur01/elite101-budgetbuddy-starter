"""Tests for the top spending category helper (ticket 03)."""

import unittest

from features import core


class TestTopSpendingCategory(unittest.TestCase):
    def test_mixed_transactions(self):
        transactions = [
            {"id": 1, "description": "Bus pass", "amount": -2.5, "category": "transport"},
            {"id": 2, "description": "Allowance", "amount": 20.0, "category": "income"},
            {"id": 3, "description": "Lunch", "amount": -6.75, "category": "food"},
            {"id": 4, "description": "Movie ticket", "amount": -12.0, "category": "fun"},
            {"id": 5, "description": "Snack", "amount": -3.25, "category": "food"},
        ]
        self.assertEqual(core.top_spending_category(transactions), "fun")

    def test_no_expenses_returns_none(self):
        transactions = [
            {"id": 1, "description": "Allowance", "amount": 20.0, "category": "income"},
        ]
        self.assertIsNone(core.top_spending_category(transactions))

    def test_tie_goes_to_first_category(self):
        transactions = [
            {"id": 1, "description": "a", "amount": -5.0, "category": "food"},
            {"id": 2, "description": "b", "amount": -5.0, "category": "fun"},
        ]
        self.assertEqual(core.top_spending_category(transactions), "food")


if __name__ == "__main__":
    unittest.main()
