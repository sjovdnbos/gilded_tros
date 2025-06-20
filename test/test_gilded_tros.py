# -*- coding: utf-8 -*-
import unittest

from src.models.item import Item
from src.gilded_tros import GildedTros


class GildedTrosTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_tros = GildedTros(items)
        gilded_tros.update_quality()
        self.assertEqual("foo", items[0].name)


if __name__ == '__main__':
    unittest.main()
