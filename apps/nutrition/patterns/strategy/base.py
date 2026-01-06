from abc import ABC, abstractmethod

class RecommendationStrategy(ABC):
    @abstractmethod
    def recommend(self, user, foods):
        pass
