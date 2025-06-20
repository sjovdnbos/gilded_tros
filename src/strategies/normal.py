from src.strategies.base import UpdateStrategy
from src.models.item import Item


class NormalItemUpdate(UpdateStrategy):
    def update(self, item: Item) -> None:
        """
        Normal items degrade in quality by 1 each day.
        If the sell_in is less than 0, they degrade by an additional 1.
        Quality cannot go below 0.
        """
        item.sell_in -= 1
        decrement = 2 if item.sell_in < 0 else 1
        item.quality = max(0, item.quality - decrement)
