# -*- coding: utf-8 -*-
from __future__ import print_function

import sys
from src.models.item import Item
from src.gilded_tros import GildedTros

if __name__ == "__main__":
    print("AXXES CODE KATA - GILDED TROS")
    items = [
        Item(name="Ring of Cleansening Code", sell_in=10, quality=20),
        Item(name="Good Wine", sell_in=2, quality=0),
        Item(name="Elixir of the SOLID", sell_in=5, quality=7),
        Item(name="B-DAWG Keychain", sell_in=0, quality=80),
        Item(name="B-DAWG Keychain", sell_in=-1, quality=80),
        Item(name="Backstage passes for Re:Factor", sell_in=15, quality=20),
        Item(name="Backstage passes for Re:Factor", sell_in=10, quality=49),
        Item(name="Backstage passes for HAXX", sell_in=5, quality=49),
        # these smelly items do not work properly yet
        Item(name="Duplicate Code", sell_in=3, quality=6),
        Item(name="Long Methods", sell_in=3, quality=6),
        Item(name="Ugly Variable Names", sell_in=3, quality=6)
    ]

    days = 2
    if len(sys.argv) > 1:
        days = int(sys.argv[1]) + 1
    for day in range(days):
        print(f" Day {day} ".center(60, "-"))
        print(f"{'Name':40s} | {'sellIn':>7s} | {'quality':>7s}")
        print("-" * 60)
        for item in items:
            print(item)
        print("\n")
        GildedTros(items).update_quality()
