from abc import ABC, abstractmethod
from .category import Category


class Clothing(ABC):
    clothing_count = 0

    def __init__(self, category: Category, name: str, price: float):
        self._category = category
        self._name = name
        self._price = price
        Clothing.clothing_count += 1

    @abstractmethod
    def description(self) -> str:
        pass #pragma: no cover

    @property
    def name(self) -> str:
     return self._name

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, new_price: float) -> None:
        if new_price < 0:
            raise ValueError('Price cannot be negative')
        self._price = new_price

    @property
    def category(self) -> Category:
        return self._category

    def __repr__(self) -> str:
        return f'{self._name!r}, ${self._price:.2f}'

    def __str__(self) -> str:
        return f'{self._category.name} {self._name} has price ${self._price:.2f}'
