"""Tests for average_balance in features/reports.py (Lesson 12)."""

import unittest

from features import reports


class TestAverageBalance(unittest.TestCase):
    def test_average_of_a_few_balances(self):
        self.assertEqual(reports.average_balance({"history": [10, 20, 30]}), 20.0)

    def test_rounds_to_one_decimal_place(self):
        # 5 / 3 = 1.666..., which rounds to 1.7
        self.assertEqual(reports.average_balance({"history": [1, 2, 2]}), 1.7)

    def test_single_balance_is_its_own_average(self):
        self.assertEqual(reports.average_balance({"history": [42]}), 42.0)

    def test_empty_history_returns_zero(self):
        self.assertEqual(reports.average_balance({"history": []}), 0.0)


if __name__ == "__main__":
    unittest.main()
