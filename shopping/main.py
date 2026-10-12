from sqlalchemy.orm import sessionmaker

from database import Base, engine, User
from products import Shirt, Pants
from cart import Cart, EmptyCartError


def main():
    # shirt = Shirt('V-Neck', 23.32)
    # print(shirt)
    # pants = Pants('Jeans', 45.11)
    # pants2 = Pants('Shorts', 34.87)
    # print(pants)
    # try:
    #     pants.price = -10
    # except ValueError:
    #     print('Error found: negative price')
    #
    # cart = Cart()
    # try:
    #     cart.remove_last_item()
    # except EmptyCartError:
    #     print('Error: empty cart')
    #
    # cart.add_to_cart(shirt)
    # cart.add_to_cart(pants)
    # cart.add_to_cart(pants2)
    # print(cart)
    # print(cart.items_by_category)

    SessionLocal = sessionmaker(engine)
    user = User(username='username1', password='secret1234', email='example@email.com')
    session = SessionLocal()
    session.add(user)
    session.commit()


def create_db():
    print("Creating all db")
    Base.metadata.create_all(bind=engine)
    print("DB created")


if __name__ == "__main__":  # pragma: no cover
    create_db()
    main()
