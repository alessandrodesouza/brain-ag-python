from abc import ABC, abstractmethod
from src.app.model.types.id.id import Id

class Entity(ABC):
    @property
    @abstractmethod
    def id(self) -> Id:
        pass
