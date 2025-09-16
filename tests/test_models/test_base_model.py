# #!/usr/bin/python3
# import unittest
# from models.base_model import BaseModel

# class TestBaseModel(unittest.TestCase):
#     my_model = BaseModel()
#     my_model.name = "My First Model"
#     my_model.my_number = 89
#     print(my_model)
#     my_model.save()
#     print(my_model)
#     my_model_json = my_model.to_dict()
#     print(my_model_json)
#     print("JSON of my_model:")
#     for key in my_model_json.keys():
#         print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))


# if __name__ == '__main__':
#     unittest.main()



#!/usr/bin/python3
import unittest
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def test_id_is_string(self):
        model = BaseModel()
        self.assertIsInstance(model.id, str)

    def test_created_and_updated_are_datetime(self):
        model = BaseModel()
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_save_updates_updated_at(self):
        model = BaseModel()
        old_updated = model.updated_at
        model.save()
        self.assertNotEqual(old_updated, model.updated_at)

    def test_to_dict_has_class_key(self):
        model = BaseModel()
        d = model.to_dict()
        self.assertEqual(d["__class__"], "BaseModel")

    def test_to_dict_datetime_format(self):
        model = BaseModel()
        d = model.to_dict()
        self.assertIsInstance(d["created_at"], str)
        self.assertIsInstance(d["updated_at"], str)
        # check ISO format compliance
        self.assertTrue("T" in d["created_at"])

    def test_str_output(self):
        model = BaseModel()
        string_output = str(model)
        self.assertIn("BaseModel", string_output)
        self.assertIn(model.id, string_output)

if __name__ == '__main__':
    unittest.main()
