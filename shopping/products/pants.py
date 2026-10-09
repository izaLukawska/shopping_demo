from .clothing import Clothing
from .category import Category


class Pants(Clothing):
    def __init__(self, name: str, price: float):
        super().__init__(Category.PANTS, name, price)

    def get_description(self) -> str:
        return f'Pants: {self._name}'
