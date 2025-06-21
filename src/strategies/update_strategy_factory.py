
from src.strategies.base import UpdateStrategy
from src.strategies.good_wine import GoodWineUpdate
from src.strategies.legendary import LegendaryUpdate
from src.strategies.backstage_pass import BackstagePassUpdate
from src.strategies.smelly import SmellyItemUpdate
from src.strategies.normal import NormalItemUpdate

class UpdateStrategyFactory:
    """
    Factory class to create update strategies based on item names.
    """
    STRATEGY_MAPPING = {
        "Good Wine": GoodWineUpdate,
        "B-DAWG Keychain": LegendaryUpdate,
        "Backstage passes for Re:Factor": BackstagePassUpdate,
        "Backstage passes for HAXX": BackstagePassUpdate,
        "Duplicate Code": SmellyItemUpdate,
        "Long Methods": SmellyItemUpdate,
        "Ugly Variable Names": SmellyItemUpdate,
    }
    @classmethod
    def create_for(cls, item_name: str) -> UpdateStrategy:
        return cls.STRATEGY_MAPPING.get(item_name, NormalItemUpdate)()
