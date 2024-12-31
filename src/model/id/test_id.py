import unittest
import uuid
from src.model.id.id import Id
from src.model.id.invalid_id_error import InvalidIdError

class TestId(unittest.TestCase):
    def test_valid_uuid(self):
        valid_uuid = '123e4567-e89b-12d3-a456-426614174000'
        id_instance = Id(valid_uuid)
        self.assertEqual(id_instance.value, valid_uuid)

    def test_invalid_uuid(self):
        invalid_uuid = 'invalid-uuid-string'
        with self.assertRaises(InvalidIdError) as context:
            Id(invalid_uuid)
        self.assertEqual(context.exception.message, "id.invalid")

    def test_create_new(self):
        id_instance = Id.create_new()
        self.assertIsInstance(id_instance, Id)
        self.assertIsInstance(id_instance.value, str)
        self.assertEqual(uuid.UUID(id_instance.value).version, 4)
