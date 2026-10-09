from products import  Shirt, Pants
from cart import Cart, EmptyCartError

def main():
    shirt = Shirt('V-Neck', 23.32)
    print(shirt)
    pants = Pants('Jeans', 45.11)
    print(pants)
    try:
        pants.price = -10
    except ValueError:
        print('Error found: negative price')

    cart = Cart()
    try:
        cart.remove_last_item()
    except EmptyCartError:
        print('Error: empty cart')

    cart.add_to_cart(shirt)
    cart.add_to_cart(pants)
    print(cart)

if __name__ == "__main__":  # pragma: no cover
    main()
