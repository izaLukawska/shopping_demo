from typing import List
from products import Clothing, Category
from .empty_cart_exception import EmptyCartError


class Cart:
    def __init__(self):
        self._items: List[Clothing] = []

    def add_to_cart(self, item: Clothing):
        self._items.append(item)

    def remove_last_item(self):
        if not self._items:
            raise EmptyCartError('Cannot remove item from empty cart')

        self._items.pop()

    @property
    def items_count(self) -> int:
        return len(self._items)

    @property
    def total_price(self) -> float:
        return sum(item.price for item in self._items)

    @property
    def items_by_category(self) -> dict[str, list[Clothing]]:
        items_by_category: dict[str, List[Clothing]] = {}
        for item in self._items:
            items_by_category.setdefault(item.category.value, []).append(item)

        return items_by_category

    def __str__(self) -> str:
        return f'Cart has {self.items_count} products with ${self.total_price:.2f}'
