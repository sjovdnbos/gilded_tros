from abc import ABC, abstractmethod
from src.models.item import Item


class BaseUpdateStrategy(ABC):
    """
    Base class for item update strategies.
    """

    MAX_QUALITY = 50
    MIN_QUALITY = 0

    def decrease_sell_in(self, item: Item) -> None:
        item.sell_in -= 1

    def increase_quality(self, item: Item, amount: int = 1) -> None:
        amount = amount * 2 if item.sell_in < 0 else amount
        item.quality = min(self.MAX_QUALITY, item.quality + amount)

    def decrease_quality(self, item: Item, amount: int = 1) -> None:
        amount = amount * 2 if item.sell_in < 0 else amount
        item.quality = max(self.MIN_QUALITY, item.quality - amount)
        
    @abstractmethod
    def update(self, item: Item) -> None:
        """
        Update the quality and sell_in of the given item.
        """
        pass
