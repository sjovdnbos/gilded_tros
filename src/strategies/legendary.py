from src.models.item import Item
from src.strategies.base import UpdateStrategy

class LegendaryUpdate(UpdateStrategy):
    def update(self, item: Item) -> None:
        """
        B-Dawg legendary items do not change in quality or sell_in.
        quality: more then 50 allowed? if not, test?
        """
        pass
