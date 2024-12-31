import re
from src.model.document.invalid_document_error import InvalidDocumentError


def is_valid_cpf(cpf: str) -> bool:
    cpf = cpf.zfill(11)
    if len(cpf) != 11 or not cpf.isdigit() or len(set(cpf)) == 1:
        return False

    def calculate_digit(digits):
        sum = 0
        for i, digit in enumerate(digits):
            sum += int(digit) * (len(digits) + 1 - i)
        remainder = sum % 11
        return '0' if remainder < 2 else str(11 - remainder)

    first_digit = calculate_digit(cpf[:9])
    second_digit = calculate_digit(cpf[:9] + first_digit)

    return cpf[-2:] == first_digit + second_digit

def is_valid_cnpj(cnpj: str) -> bool:
    cnpj = cnpj.zfill(14)
    if len(cnpj) != 14 or not cnpj.isdigit() or len(set(cnpj)) == 1:
        return False

    def calculate_digit(digits, weights):
        sum = 0
        for i, digit in enumerate(digits):
            sum += int(digit) * weights[i]
        remainder = sum % 11
        return '0' if remainder < 2 else str(11 - remainder)

    first_weights = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    second_weights = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    first_digit = calculate_digit(cnpj[:12], first_weights)
    second_digit = calculate_digit(cnpj[:12] + first_digit, second_weights)

    return cnpj[-2:] == first_digit + second_digit

class Document:
    def __init__(self, value: str):
        value = re.sub(r'\D', '', value)
        
        if is_valid_cpf(value):
            self._value = value.zfill(11)
        elif is_valid_cnpj(value):
            self._value = value.zfill(14)
        else:
            raise InvalidDocumentError()

    @staticmethod
    def try_parse(value: str) -> bool:
        try:
            Document(value)
            return True
        except InvalidDocumentError:
            return False

    @property
    def value(self):
        return self._value

    def __str__(self):
        return f"Document: {self._value}"
