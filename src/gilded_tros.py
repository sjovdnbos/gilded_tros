# -*- coding: utf-8 -*-
from typing import List
from src.strategies.update_strategy_factory import UpdateStrategyFactory
from src.models.item import Item

class GildedTros(object):

    def __init__(self, items: List[Item]) -> None:
        self.items = items

    def update_quality(self) -> None:
        """
        Update quality and sell_in for all items using their respective strategies.
        """
        for item in self.items:
            strategy = UpdateStrategyFactory.create_for(item.name)
            strategy.update(item)
