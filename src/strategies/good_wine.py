from src.models.item import Item
from src.strategies.base import UpdateStrategy

class GoodWineUpdate(UpdateStrategy):
    def update(self, item: Item) -> None:
        """
        Good wine items increase in quality as they age.
        The quality increases by 1 each day, 2 if the sell_in is less than 0.
        """
        item.sell_in -= 1
        increment = 2 if item.sell_in < 0 else 1
        item.quality = min(50, item.quality + increment)
