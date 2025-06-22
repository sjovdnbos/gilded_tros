import unittest
from src.models.item import Item
from src.strategies.smelly import SmellyItemUpdateStrategy

class SmellyItemUpdateTests(unittest.TestCase):

    def test_quality_degrades_before_expiry(self):
        """
        Smelly items lose 2 quality per day before sell_in date.
        """
        item = Item("Long Methods", sell_in=5, quality=10)
        strategy = SmellyItemUpdateStrategy()
        strategy.update(item)

        self.assertEqual(item.sell_in, 4)
        self.assertEqual(item.quality, 8)

    def test_quality_degrades_after_expiry(self):
        """
        Smelly items lose 4 quality per day after sell_in date.
        """
        item = Item("Ugly Variable Names", sell_in=0, quality=10)
        strategy = SmellyItemUpdateStrategy()
        strategy.update(item)

        self.assertEqual(item.sell_in, -1)
        self.assertEqual(item.quality, 6)

    def test_quality_never_negative(self):
        """
        Smelly item quality should never go below 0.
        """
        item = Item("Duplicate Code", sell_in=1, quality=1)
        strategy = SmellyItemUpdateStrategy()
        strategy.update(item)

        self.assertEqual(item.sell_in, 0)
        self.assertEqual(item.quality, 0)

    def test_quality_never_negative_even_when_expired(self):
        """
        Smelly item quality should never go below 0, even after expiration.
        """
        item = Item("Duplicate Code", sell_in=-1, quality=3)
        strategy = SmellyItemUpdateStrategy()
        strategy.update(item)

        self.assertEqual(item.sell_in, -2)
        self.assertEqual(item.quality, 0)
