import unittest
from datetime import datetime
from src.model.document.document import Document
from src.model.id.id import Id
from src.model.farmer.farmer import Farmer
from src.model.farmer.farmer_create_error import FarmerCreateError

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
        self.assertEqual(farmer.id, self.id)
        self.assertEqual(farmer.document.value, "12345678909")
        self.assertEqual(farmer.name, self.name.upper())
        self.assertEqual(farmer.created_at, self.created_at)
        self.assertEqual(farmer.updated_at, self.updated_at)

    def test_create_new_valid_farmer(self):
        farmer = Farmer.create_new(document=self.document, name=self.name)
        
        self.assertIsInstance(farmer, Farmer)
        self.assertIsInstance(farmer.id, Id)
        self.assertIsInstance(farmer.document, Document)
        self.assertEqual(farmer.document.value, self.document)
        self.assertEqual(farmer.name, self.name.upper())
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
        self.assertEqual(farmer.name, "JANE DOE")
        self.assertIsNotNone(farmer.updated_at)
        self.assertGreater(farmer.updated_at, farmer.created_at)

    def test_update_invalid_farmer_data(self):
        farmer = Farmer.create_new(document=self.document, name=self.name)
        
        with self.assertRaises(FarmerCreateError) as context:
            farmer.update(document=self.invalid_document, name=self.invalid_name)
        
        self.assertIn("document.invalid", context.exception.messages)
        self.assertIn("name.invalid", context.exception.messages)
