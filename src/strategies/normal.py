from src.strategies.base import UpdateStrategy
from src.models.item import Item


class NormalItemUpdate(UpdateStrategy):
    def update(self, item: Item) -> None:
        item.sell_in -= 1
        decrement = 2 if item.sell_in < 0 else 1
        item.quality = max(0, item.quality - decrement)
