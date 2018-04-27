import unittest

from src.airports import Airports

class TestAirports(unittest.TestCase):

    def test_distance(self):
        airports = Airports("resources/cities.yml")
        self.assertEqual(412, int(airports.get_distance("Paris", "Lyon")))

if __name__ == '__main__':
    unittest.main()