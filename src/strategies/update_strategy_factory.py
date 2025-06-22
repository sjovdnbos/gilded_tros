
from src.strategies.base import BaseUpdateStrategy
from src.strategies.good_wine import GoodWineUpdateStrategy
from src.strategies.legendary import LegendaryUpdateStrategy
from src.strategies.backstage_pass import BackstagePassUpdateStrategy
from src.strategies.smelly import SmellyItemUpdateStrategy
from src.strategies.normal import NormalItemUpdateStrategy

class UpdateStrategyFactory:
    """
    Factory class to create update strategies based on item names.
    """
    STRATEGY_MAPPING = {
        "Good Wine": GoodWineUpdateStrategy,
        "B-DAWG Keychain": LegendaryUpdateStrategy,
        "Backstage passes for Re:Factor": BackstagePassUpdateStrategy,
        "Backstage passes for HAXX": BackstagePassUpdateStrategy,
        "Duplicate Code": SmellyItemUpdateStrategy,
        "Long Methods": SmellyItemUpdateStrategy,
        "Ugly Variable Names": SmellyItemUpdateStrategy,
    }
    @classmethod
    def create_for(cls, item_name: str) -> BaseUpdateStrategy:
        return cls.STRATEGY_MAPPING.get(item_name, NormalItemUpdateStrategy)()
