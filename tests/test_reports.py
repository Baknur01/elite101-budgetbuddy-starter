import unittest
from features import reports

class TestReports(unittest.TestCase):
    def test_average_balance(self):
        data = {"history": [100.0, 200.0, 300.0]}
        self.assertEqual(reports.average_balance(data), 200.0)

    def test_average_balance_empty(self):
        data = {"history": []}
        self.assertEqual(reports.average_balance(data), 0.0)

if __name__ == "__main__":
    unittest.main()