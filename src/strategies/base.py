from abc import ABC, abstractmethod
from src.models.item import Item


class UpdateStrategy(ABC):
    """Base class for item update strategies."""

    @abstractmethod
    def update(self, item: Item) -> None:
        """Update the quality and sell_in of the given item."""
        pass
