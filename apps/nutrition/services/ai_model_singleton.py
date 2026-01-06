class AIModelSingleton:
    """
    Singleton for adaptive smart diet engine
    """

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AIModelSingleton, cls).__new__(cls)
            cls._instance._init_model()
        return cls._instance

    def _init_model(self):
        # وزن اولیه استراتژی‌ها (قابل توسعه)
        self.strategy_weights = {
            "low_calorie": 1.0,
            "high_protein": 1.0,
            "economic": 1.0,
        }

    def reward(self, strategy_name: str):
        if strategy_name in self.strategy_weights:
            self.strategy_weights[strategy_name] += 0.1

    def penalize(self, strategy_name: str):
        if strategy_name in self.strategy_weights:
            self.strategy_weights[strategy_name] -= 0.1

    def get_weight(self, strategy_name: str) -> float:
        return self.strategy_weights.get(strategy_name, 1.0)
