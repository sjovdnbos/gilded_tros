import unittest
from src.models.item import Item
from src.strategies.backstage_pass import BackstagePassUpdate


class BackstagePassUpdateTests(unittest.TestCase):

    def test_quality_increase_by_1_above_10_days(self):
        """
        Should increase quality by 1 when SellIn > 10.
        """
        item = Item("Backstage passes", sell_in=15, quality=20)
        strategy = BackstagePassUpdate()
        strategy.update(item)

        self.assertEqual(item.sell_in, 14)
        self.assertEqual(item.quality, 21)

    def test_quality_increase_by_2_between_10_and_6_days(self):
        """
        Should increase quality by 2 when SellIn is between 10 and 6.
        """
        item = Item("Backstage passes", sell_in=10, quality=20)
        strategy = BackstagePassUpdate()
        strategy.update(item)

        self.assertEqual(item.sell_in, 9)
        self.assertEqual(item.quality, 22)

    def test_quality_increase_by_3_between_5_and_1_days(self):
        """
        Should increase quality by 3 when SellIn is between 5 and 1.
        """
        item = Item("Backstage passes", sell_in=5, quality=20)
        strategy = BackstagePassUpdate()
        strategy.update(item)

        self.assertEqual(item.sell_in, 4)
        self.assertEqual(item.quality, 23)

    def test_quality_drops_to_0_after_concert(self):
        """
        Should drop quality to 0 when SellIn is 0 or less.
        """
        item = Item("Backstage passes", sell_in=0, quality=25)
        strategy = BackstagePassUpdate()
        strategy.update(item)

        self.assertEqual(item.sell_in, -1)
        self.assertEqual(item.quality, 0)

    def test_quality_never_exceeds_50(self):
        """Quality should never exceed 50"""
        item1 = Item("Backstage passes", sell_in=15, quality=50)
        item2 = Item("Backstage passes", sell_in=10, quality=49)
        item3 = Item("Backstage passes", sell_in=5, quality=48)
        strategy = BackstagePassUpdate()
        strategy.update(item1)
        strategy.update(item2)
        strategy.update(item3)
        
        self.assertEqual(item1.quality, 50)
        self.assertEqual(item2.quality, 50)
        self.assertEqual(item3.quality, 50)
