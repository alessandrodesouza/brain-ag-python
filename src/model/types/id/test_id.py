import unittest
import uuid
from src.model.types.id.id import Id
from src.model.types.id.invalid_id_error import InvalidIdError

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

    def test_try_parse_valid(self):
        valid_uuid = '123e4567-e89b-12d3-a456-426614174000'
        result = Id.try_parse(valid_uuid)
        self.assertTrue(result)

    def test_try_parse_invalid(self):
        invalid_uuid = 'invalid-uuid-string'
        result = Id.try_parse(invalid_uuid)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
