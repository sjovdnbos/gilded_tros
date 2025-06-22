from src.models.item import Item
from src.strategies.base import BaseUpdateStrategy


class NormalItemUpdateStrategy(BaseUpdateStrategy):
    def update(self, item: Item) -> None:
        """
        Normal items degrade in quality by 1 each day.
        """
        self.decrease_sell_in(item)
        self.decrease_quality(item)
