from src.models.item import Item
from src.strategies.base import BaseUpdateStrategy

class SmellyItemUpdateStrategy(BaseUpdateStrategy):
    def update(self, item: Item) -> None:
        """
        Smelly items degrade in quality by 2 each day.
        """
        self.decrease_sell_in(item)
        self.decrease_quality(item, 2)
