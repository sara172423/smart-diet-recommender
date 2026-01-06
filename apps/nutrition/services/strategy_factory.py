from ..patterns.strategy.low_calorie import LowCalorieStrategy
from ..patterns.strategy.high_protein import HighProteinStrategy
from ..patterns.strategy.economic import EconomicStrategy


class StrategyFactory:

    @staticmethod
    def get_strategy(strategy_type):
        if strategy_type == 'low':
            return LowCalorieStrategy()
        elif strategy_type == 'high_protein':
            return HighProteinStrategy()
        elif strategy_type == 'economic':
            return EconomicStrategy()
        else:

            return LowCalorieStrategy()
