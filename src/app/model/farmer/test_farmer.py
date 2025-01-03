import unittest
from datetime import datetime
from src.app.model.farmer.farmer_parser_error import FarmerParserError
from src.app.model.farmer.farmer_update_error import FarmerUpdateError
from src.app.model.types.document.document import Document
from src.app.model.types.id.id import Id
from src.app.model.farmer.farmer import Farmer
from src.app.model.farmer.farmer_create_error import FarmerCreateError
from src.app.model.types.name.name import Name

class TestFarmer(unittest.TestCase):
    def setUp(self):
        self.id = "2d83ea5a-75d1-4b72-bda7-5132106ea063"
        self.document = "12345678909"
        self.name = "John Doe"
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.invalid_document = "11111111111111"
        self.invalid_name = ""

    def test_parse_valid_farmer(self):
        farmer = Farmer(id=self.id, document=self.document, name=self.name, created_at=self.created_at, updated_at=self.updated_at)

        self.assertIsInstance(farmer, Farmer)
        self.assertIsInstance(farmer.id, Id)
        self.assertEqual(farmer.id.value, self.id)
        self.assertIsInstance(farmer.document, Document)
        self.assertEqual(farmer.document.value, "12345678909")
        self.assertIsInstance(farmer.name, Name)
        self.assertEqual(farmer.name.value, self.name.upper())
        self.assertEqual(farmer.created_at, self.created_at)
        self.assertEqual(farmer.updated_at, self.updated_at)

    def test_parse_invalid_farmer(self):
        with self.assertRaises(FarmerParserError) as context:
            Farmer(id=self.id, document=self.invalid_document, name=self.name, created_at=self.created_at, updated_at=self.updated_at)

        self.assertIn("document.invalid", context.exception.messages)
        self.assertEqual(len(context.exception.messages), 1)

    def test_create_new_valid_farmer(self):
        farmer = Farmer.create_new(document=self.document, name=self.name)
        
        self.assertIsInstance(farmer, Farmer)
        self.assertIsInstance(farmer.id, Id)
        self.assertIsInstance(farmer.document, Document)
        self.assertEqual(farmer.document.value, self.document)
        self.assertIsInstance(farmer.name, Name)
        self.assertEqual(farmer.name.value, self.name.upper())
        self.assertIsInstance(farmer.created_at, datetime)
        self.assertIsNone(farmer.updated_at)

    def test_create_new_invalid_farmer(self):
        with self.assertRaises(FarmerCreateError) as context:
            Farmer.create_new(document=self.invalid_document, name=self.invalid_name)
        
        self.assertIn("document.invalid", context.exception.messages)
        self.assertIn("name.invalid", context.exception.messages)

    def test_update_valid_farmer_data(self):
        farmer = Farmer.create_new(document=self.document, name=self.name)
        
        new_document = "98765432100"
        new_name = "Jane Doe"
        farmer.update(document=new_document, name=new_name)
        
        self.assertEqual(farmer.document.value, "98765432100")
        self.assertEqual(farmer.name.value, "JANE DOE")
        self.assertIsNotNone(farmer.updated_at)
        self.assertGreater(farmer.updated_at, farmer.created_at)

    def test_update_invalid_farmer_data(self):
        farmer = Farmer.create_new(document=self.document, name=self.name)
        
        with self.assertRaises(FarmerUpdateError) as context:
            farmer.update(document=self.invalid_document, name=self.invalid_name)
        
        self.assertIn("document.invalid", context.exception.messages)
        self.assertIn("name.invalid", context.exception.messages)

if __name__ == '__main__':
    unittest.main()
