from src.models.item import Item
from src.strategies.base import BaseUpdateStrategy

class LegendaryUpdateStrategy(BaseUpdateStrategy):
    def update(self, item: Item) -> None:
        """
        B-Dawg legendary items do not change in quality or sell_in.
        """
        pass
