from abc import ABC
from .category import Category


class Clothing(ABC):
    clothing_count = 0

    def __init__(self, category: Category, name: str, price: float):
        self._category = category
        self._name = name
        self._price = price
        Clothing.clothing_count += 1

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, new_price: float) -> None:
        if new_price < 0:
            raise ValueError('Price cannot be negative')
        self.price = new_price

    @property
    def category(self) -> Category:
        return self._category

    def __str__(self) -> str:
        return f'{self._category.name} {self._name} has price ${self._price:.2f}'
