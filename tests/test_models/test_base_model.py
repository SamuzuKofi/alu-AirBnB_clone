#!/usr/bin/python3
import unittest
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

class TestBaseModel(unittest.TestCase):
    def test_add(self):
        result = add(2, 3)
        self.assertEqual(result, 5)

    def test_subtract(self):
        result = subtract(5, 3)
        self.assertEqual(result, 2)

    def test_multiply(self):
        result = multiply(2, 3)
        self.assertEqual(result, 6)

    def test_divide(self):
        result = divide(6, 3)
        self.assertEqual(result, 2)

    def test_modulus(self):
        result = modulus(5, 3)
        self.assertEqual(result, 2)
    def test_power(self):
        result = power(2, 3)
        self.assertEqual(result, 8)

if __name__ == '__main__':
    unittest.main()