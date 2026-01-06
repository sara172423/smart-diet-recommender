from abc import ABC, abstractmethod

class FoodComponent(ABC):

    @abstractmethod
    def get_calories(self):
        pass

    @abstractmethod
    def get_description(self):
        pass
