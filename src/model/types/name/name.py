from .invalid_name_error import InvalidNameError

class Name:
    def __init__(self, value: str):
        if not isinstance(value, str) or not (1 <= len(value) <= 255):
            raise InvalidNameError()
        self._value = value.upper() 

    @staticmethod
    def parse(value: str) -> 'Name':
        return Name(value)

    @staticmethod
    def try_parse(value: str) -> bool:
        try:
            Name(value)
            return True
        except InvalidNameError:
            return False

    @property
    def value(self) -> str:
        return self._value

    def __str__(self):
        return f"Name: {self._value}"
