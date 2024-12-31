import unittest
from src.model.document.document import Document
from src.model.document.invalid_document_error import InvalidDocumentError

class TestDocument(unittest.TestCase):
    def test_valid_cpf(self):
        valid_cpf = '12345678909'
        doc = Document(valid_cpf)
        self.assertEqual(doc.value, valid_cpf.zfill(11))

    def test_valid_formatted_cpf(self):
        valid_cpf = '60.406.530-27'
        doc = Document(valid_cpf)
        self.assertEqual(doc.value, '06040653027')

    def test_invalid_cpf(self):
        invalid_cpf = '12345678900'
        with self.assertRaises(InvalidDocumentError) as context:
            Document(invalid_cpf)
        self.assertEqual(context.exception.message, 'document.invalid')

    def test_valid_cnpj(self):
        valid_cnpj = '12345678000195'
        doc = Document(valid_cnpj)
        self.assertEqual(doc.value, valid_cnpj.zfill(14))

    def test_valid_formatted_cnpj(self):
        valid_cnpj = '7.525.850/0001-52'
        doc = Document(valid_cnpj)
        self.assertEqual(doc.value, '07525850000152')

    def test_invalid_cnpj(self):
        invalid_cnpj = '12345678000196'
        with self.assertRaises(InvalidDocumentError) as context:
            Document(invalid_cnpj)
        self.assertEqual(context.exception.message, 'document.invalid')

    def test_try_parse_valid_cpf(self):
        valid_cpf = '12345678909'
        self.assertTrue(Document.try_parse(valid_cpf))

    def test_try_parse_invalid_cpf(self):
        invalid_cpf = '12345678900'
        self.assertFalse(Document.try_parse(invalid_cpf))

    def test_try_parse_valid_cnpj(self):
        valid_cnpj = '12345678000195'
        self.assertTrue(Document.try_parse(valid_cnpj))

    def test_try_parse_invalid_cnpj(self):
        invalid_cnpj = 'invalid_cnpj'
        self.assertFalse(Document.try_parse(invalid_cnpj))
