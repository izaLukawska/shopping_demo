from typing import Protocol

class Payable(Protocol):
    def pay(self, amount: float) -> str:
        ...
