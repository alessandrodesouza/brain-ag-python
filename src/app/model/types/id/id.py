import uuid
from src.app.model.types.id.invalid_id_error import InvalidIdError

class Id:
    def __init__(self, value: str):
        try:
            val = uuid.UUID(value, version=4)
            if val.version != 4:
                raise InvalidIdError()
        except ValueError:
            raise InvalidIdError()
        
        self._value = value

    @staticmethod
    def create_new() -> 'Id':
        new_uuid = uuid.uuid4()
        return Id(str(new_uuid))

    @staticmethod
    def try_parse(value: str) -> bool:
        try:
            Id(value)
            return True
        except InvalidIdError:
            return False

    @property
    def value(self) -> str:
        return self._value

    def __str__(self):
        return f"Id: {self._value}"
