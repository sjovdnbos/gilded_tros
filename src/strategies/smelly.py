from src.models.item import Item
from src.strategies.base import UpdateStrategy

class SmellyItemUpdate(UpdateStrategy):
    def update(self, item: Item) -> None:
        """
        Smelly items degrade in quality by 2 each day.
        If the sell_in is less than 0, they degrade by an additional 2.
        """
        item.sell_in -= 1
        decrement = 4 if item.sell_in < 0 else 2
        item.quality = max(0, item.quality - decrement)
