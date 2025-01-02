from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field, ValidationError, field_validator
from src.model.document.document import Document
from src.model.entity import Entity
from src.model.id.id import Id
from src.model.farmer.farmer_create_error import FarmerCreateError

class FarmerModel(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    
    id: Optional[str] = None
    document: str
    name: str
    created_at: datetime
    updated_at: Optional[datetime] = None

    @field_validator("id")
    def validate_id(cls, value):
        if value is None:
            return value
        if not isinstance(value, str):
            raise ValueError("Id must be a valid uuid")
        if not Id.try_parse(value):
            raise ValueError("Id must be a valid uuid")
        return value

    @field_validator("name")
    def validate_and_format_name(cls, value):
        if not isinstance(value, str) or not (1 <= len(value) <= 255):
            raise ValueError("Name must be a string with length between 1 and 255 characters")
        return value.upper() 

    @field_validator("document")
    def validate_document(cls, value):
        if not isinstance(value, str):
            raise ValueError("Document must be a valid ccpf or cnpj")
        if not Document.try_parse(value):
            raise ValueError("Document must be a valid ccpf or cnpj")
        return value
    
    @field_validator("created_at")
    def validate_created_at(cls, value):
        if not isinstance(value, datetime):
            raise ValueError("CreatedAt must be a valid datetime")
        return value

    @field_validator("updated_at")
    def validate_updated_at(cls, value):
        if value is not None and not isinstance(value, datetime):
            raise ValueError("UpdatedAt must be a valid datetime")
        return value

class Farmer(Entity):
    def __init__(
            self,
            document: str,
            name: str,
            id: Optional[str] = None,
            created_at: Optional[datetime] = None,
            updated_at: Optional[datetime] = None
        ):
        created_at: datetime = created_at if created_at is not None else datetime.now()

        try:
            validated_data = FarmerModel(id=id, document=document, name=name, created_at=created_at, updated_at=updated_at)
        except ValidationError as e:
            error_messages = [f"{err['loc'][0]}.invalid" for err in e.errors()]
            raise FarmerCreateError(messages=error_messages)
        
        self._id = id if id is not None else Id.create_new()
        self._document = Document(validated_data.document)
        self._name = validated_data.name
        self._created_at = validated_data.created_at
        self._updated_at = validated_data.updated_at

    @staticmethod
    def create_new(document: str, name: str) -> 'Farmer':
        return Farmer(document=document, name=name)

    def update(self, document: str, name: str) -> None:
        errors = []

        try:
            document = FarmerModel.validate_document(document)
        except ValueError:
            errors.append("document.invalid")
        try:
            name = FarmerModel.validate_and_format_name(name)
        except ValueError:
            errors.append("name.invalid")

        if errors:
            raise FarmerCreateError(messages=errors)
        
        self._document = Document(document)
        self._name = name
        self._updated_at = datetime.now()
    
    @property
    def id(self) -> Id:
        return self._id

    @property
    def document(self) -> Document:
        return self._document

    @property
    def name(self) -> str:
        return self._name

    @property
    def created_at(self) -> datetime:
        return self._created_at

    @property
    def updated_at(self) -> Optional[datetime]:
        return self._updated_at

    def __str__(self):
        return f"Farmer: {self._id} {self._document} {self._name}"
