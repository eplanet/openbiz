import unittest

from src.company import Company

class TestCompany(unittest.TestCase):

    def test_movements(self):
        c = Company("Air France")

if __name__ == '__main__':
    unittest.main()