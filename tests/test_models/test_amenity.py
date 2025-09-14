import unittest
from models.amenity import add


class TestAmenity(unittest.TestCase):
    def test_add(self):
        result = add(2, 3)
        self.assertEqual(result, 5)