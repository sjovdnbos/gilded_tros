from src.models.item import Item
from src.strategies.base import UpdateStrategy

class GoodWineUpdate(UpdateStrategy):
    def update(self, item: Item) -> None:
        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality = min(50, item.quality + 2)
        else:
            item.quality = min(50, item.quality + 1)
