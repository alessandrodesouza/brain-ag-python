from abc import ABC, abstractmethod

from src.app.model.farmer.farmer import Farmer
from src.app.model.types.id.id import Id

class FarmerRepository(ABC):
    def craate(self, farmer: Farmer) -> Id:
        pass

    def update(self, farmer: Farmer) -> None:
        pass
    
    def get_by_id(self, farmer_id: Id) -> Farmer:
        pass