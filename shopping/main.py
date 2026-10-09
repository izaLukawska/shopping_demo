from products import  Shirt, Pants

def main():
    shirt = Shirt('V-Neck', 23.32)
    print(shirt)
    pants = Pants('Jeans', 45.11)
    print(pants)
    try:
        pants.price = -10
    except ValueError:
        print('Error found: negative price')

if __name__ == "__main__":  # pragma: no cover
    main()
