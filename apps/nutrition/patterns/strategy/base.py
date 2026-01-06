from abc import ABC, abstractmethod

class RecommendationStrategy(ABC):

    @abstractmethod
    def recommend(self, user):
        """
        ورودی: user
        خروجی: لیست غذاهای پیشنهادی
        """
        pass
