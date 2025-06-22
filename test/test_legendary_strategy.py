import unittest
from src.models.item import Item
from src.strategies.legendary import LegendaryUpdateStrategy


class LegendaryUpdateTests(unittest.TestCase):

    def test_remains_unchanged(self):
        """
        Should not decrement the sell_in value or quality value for legendary item.
        """
        item = Item("B-DAWG Keychain", sell_in=15, quality=80)
        strategy = LegendaryUpdateStrategy()
        strategy.update(item)

        self.assertEqual(item.sell_in, 15)
        self.assertEqual(item.quality, 80)
