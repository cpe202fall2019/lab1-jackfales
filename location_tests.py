import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        loc2 = Location("Paris", 48.9, 2.4)
        loc3 = loc
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)") # Test for equality
        self.assertNotEqual(repr(loc), repr(loc2)) # Test for inequality
        self.assertEqual(repr(loc), repr(loc3)) # Test for exact copies of objects

    def test_eq(self):
        loc = Location("SLO", 35.3, -120.7)
        loc2 = Location("Paris", 48.9, 2.4)
        loc3 = loc
        loc4 = Location("SLO", 34.3, -120.7)
        self.assertEqual(loc, loc3) # Test for equality
        self.assertNotEqual(loc, loc2) # Test for inequality
        self.assertEqual(loc, loc3) # Test for exact copies of objects
        self.assertNotEqual(loc, loc4) # Test for inequality when similar

    # Add more tests!

if __name__ == "__main__":
        unittest.main()
