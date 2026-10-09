from .clothing import Clothing
from .category import Category


class Shirt(Clothing):
    def __init__(self,  name: str, price: float):
        super().__init__(Category.SHIRT, name, price)
