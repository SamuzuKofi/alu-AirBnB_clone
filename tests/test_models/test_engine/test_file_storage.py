import unittest
from models.engine.file_storage import add


class TestFileStorage(unittest.TestCase):
    def test_add(self):
        result = add(2, 3)
        self.assertEqual(result, 5)