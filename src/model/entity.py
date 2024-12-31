from abc import ABC, abstractmethod
from src.model.id.id import Id

class Entity(ABC):
    @property
    @abstractmethod
    def id(self) -> Id:
        pass
