from abc import ABC, abstractmethod

class FoodFactory(ABC):
    @abstractmethod
    def create_food(self, data):
        pass
