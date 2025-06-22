import unittest
from src.models.item import Item
from src.strategies.good_wine import GoodWineUpdateStrategy

class GoodWineUpdateTests(unittest.TestCase):

    def test_increase_quality_by_one(self):
        """
        Should increase quality by 1 when quality is below 50.
        """
        item = Item("Good Wine", sell_in=10, quality=20)
        strategy = GoodWineUpdateStrategy()
        strategy.update(item)

        self.assertEqual(item.sell_in, 9)
        self.assertEqual(item.quality, 21)

    def test_quality_not_above_50(self):
        """
        Should cap quality at 50 when it is 50 or more.
        """
        item = Item("Good Wine", sell_in=5, quality=50)
        strategy = GoodWineUpdateStrategy()
        strategy.update(item)

        self.assertEqual(item.sell_in, 4)
        self.assertEqual(item.quality, 50)

    def test_quality_increase_near_cap(self):
        """
        Should cap quality at 50 when quality is 49.
        """
        item = Item("Good Wine", sell_in=3, quality=49)
        strategy = GoodWineUpdateStrategy()
        strategy.update(item)

        self.assertEqual(item.sell_in, 2)
        self.assertEqual(item.quality, 50)
        
    def test_quality_increase_after_sell_date(self):
        """
        Should increase quality by 2 after sell date, capped at 50.
        """
        item = Item("Good Wine", sell_in=0, quality=48)
        strategy = GoodWineUpdateStrategy()
        strategy.update(item)

        self.assertEqual(item.sell_in, -1)
        self.assertEqual(item.quality, 50)
