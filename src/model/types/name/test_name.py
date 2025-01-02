import unittest
from .name import Name
from .invalid_name_error import InvalidNameError

class TestName(unittest.TestCase):

    def setUp(self):
        self.valid_name = "ValidName"
        self.invalid_name_empty = ""
        self.invalid_name_too_long = "a" * 256

    def test_valid_name(self):
        name = Name(self.valid_name)
        self.assertEqual(name.value, "VALIDNAME")

    def test_invalid_name_empty(self):
        with self.assertRaises(InvalidNameError) as context:
            Name(self.invalid_name_empty)
        self.assertEqual(context.exception.message, "name.invalid")

    def test_invalid_name_too_long(self):
        with self.assertRaises(InvalidNameError) as context:
            Name(self.invalid_name_too_long)
        self.assertEqual(context.exception.message, "name.invalid")

    def test_parse_valid_name(self):
        name = Name.parse(self.valid_name)
        self.assertEqual(name.value, "VALIDNAME")

    def test_parse_invalid_name(self):
        with self.assertRaises(InvalidNameError) as context:
            Name.parse(self.invalid_name_empty)
        self.assertEqual(context.exception.message, "name.invalid")

    def test_try_parse_valid_name(self):
        self.assertTrue(Name.try_parse(self.valid_name))

    def test_try_parse_invalid_name(self):
        self.assertFalse(Name.try_parse(self.invalid_name_empty))

if __name__ == '__main__':
    unittest.main()
