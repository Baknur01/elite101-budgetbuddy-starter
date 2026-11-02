"""Tests for the average balance report (Lesson 12)."""

import unittest

from features import reports


class TestAverageBalance(unittest.TestCase):
    def test_average_of_sample_history(self):
        self.assertEqual(reports.average_balance({"history": [50.0, 45.0, 60.0]}), 51.7)

    def test_single_balance(self):
        self.assertEqual(reports.average_balance({"history": [20.0]}), 20.0)

    def test_empty_history_returns_zero(self):
        self.assertEqual(reports.average_balance({"history": []}), 0.0)


if __name__ == "__main__":
    unittest.main()
