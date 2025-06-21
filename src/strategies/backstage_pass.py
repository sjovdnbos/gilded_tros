from src.models.item import Item
from src.strategies.base import UpdateStrategy

class BackstagePassUpdate(UpdateStrategy):
    def update(self, item: Item) -> None:
        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality = 0
        else:
            if item.quality < 50:
                item.quality += 1
                if item.sell_in < 10 and item.quality < 50:
                    item.quality += 1   # increase by 2    
                if item.sell_in < 5 and item.quality < 50:
                    item.quality += 1   # increase by 3
