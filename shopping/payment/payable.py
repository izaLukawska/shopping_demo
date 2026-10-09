from typing import Protocol

class Payable(Protocol):
    def pay(self, price: float) -> bool:
        ...
