from src.models.item import Item
from src.strategies.base import BaseUpdateStrategy

class GoodWineUpdateStrategy(BaseUpdateStrategy):
    def update(self, item: Item) -> None:
        """
        Good wine items increase in quality as they age.
        """
        self.decrease_sell_in(item)
        self.increase_quality(item)
