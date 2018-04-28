import unittest

from openbiz.airports import Airport, Airports

class TestAirports(unittest.TestCase):

    def test_distance(self):
        airports = Airports("resources/airports.yml")
        self.assertEqual(412, int(airports.get_distance("Paris", "Lyon")))
        self.assertEqual(airports.get_rounded_distance("Paris", "Lyon"), int(airports.get_distance("Paris", "Lyon")))

if __name__ == '__main__':
    unittest.main()