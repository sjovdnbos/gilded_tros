from src.models.item import Item
from src.strategies.base import BaseUpdateStrategy

class BackstagePassUpdateStrategy(BaseUpdateStrategy):
    def update(self, item: Item) -> None:
        """
        Backstage passes increase in quality as the date approaches, 
        but drop to 0 quality after the conference.
        """
        self.decrease_sell_in(item)

        if item.sell_in < 0:
            item.quality = 0
        else:
            self.increase_quality(item)
            if item.sell_in < 10:
                self.increase_quality(item)
            if item.sell_in < 5:
                self.increase_quality(item)
