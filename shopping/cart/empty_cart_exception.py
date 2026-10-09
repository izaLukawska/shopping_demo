class EmptyCartError(Exception):
    def __init__(self, message: str = "Cannot perform operation: Cart is empty."):
        super().__init__(message)
