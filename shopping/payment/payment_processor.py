from .payable import Payable


class PaymentProcessor[T: Payable]:
    def __init__(self, payment_method: T):
        self._payment_method = payment_method

    def process(self, amount: float) -> str:
        return self._payment_method.pay(amount)
