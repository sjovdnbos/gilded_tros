import unittest
from src.models.item import Item
from src.strategies.normal import NormalItemUpdate

class TestNormalItemUpdate(unittest.TestCase):

    def test_normal_item_update_before_sell_date(self):
        """
        Every day, sell_in and quality decrease by 1
        """
        item = Item(name="Normal Item", sell_in=10, quality=20)
        strategy = NormalItemUpdate()
        strategy.update(item)

        self.assertEqual(item.sell_in, 9)
        self.assertEqual(item.quality, 19)


    def test_normal_item_update_after_sell_date(self):
        """
        After sell date, quality decreases by 2
        """
        item = Item(name="Normal Item", sell_in=0, quality=20)
        strategy = NormalItemUpdate()
        strategy.update(item)

        self.assertEqual(item.sell_in, -1)
        self.assertEqual(item.quality, 18)


    def test_normal_item_quality_never_negative(self):
        """
        Quality should never be negative
        """
        item = Item(name="Normal Item", sell_in=5, quality=0)
        strategy = NormalItemUpdate()
        strategy.update(item)

        self.assertEqual(item.sell_in, 4)
        self.assertEqual(item.quality, 0)
