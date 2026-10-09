import pytest

from shopping.products import Shirt, Pants
from shopping.cart import Cart, EmptyCartError


@pytest.fixture
def empty_cart() -> Cart:
    return Cart()


@pytest.fixture
def base_cart() -> Cart:
    cart = Cart()
    shirt1 = Shirt('Crew neck1', 12.20)
    shirt2 = Shirt('Crew neck2', 32.00)
    pants = Pants('Jeans', 45.12)
    cart.add_to_cart(shirt1)
    cart.add_to_cart(shirt2)
    cart.add_to_cart(pants)
    return cart


def test_cart_initialization_and_properties():
    # when
    cart = Cart()
    # then
    assert cart.items_count == 0


def test_add_to_cart(empty_cart: Cart):
    # given
    shirt = Shirt('Crew neck', 12.20)
    # when
    empty_cart.add_to_cart(shirt)
    # then
    assert empty_cart.items_count == 1
    assert shirt in empty_cart.items_by_category["shirt"]


def test_remove_last_item_success(base_cart: Cart):
    # when
    base_cart.remove_last_item()
    # then
    assert base_cart.items_count == 2


def test_items_count(base_cart: Cart):
    # then
    assert base_cart.items_count == 3


def test_total_price(base_cart: Cart):
    # then
    assert base_cart.total_price == 89.32


def test_items_by_category(base_cart: Cart):
    # when
    items_by_category = base_cart.items_by_category

    # then
    assert [item.name for item in items_by_category["shirt"]] == [
        "Crew neck1",
        "Crew neck2",
    ]
    assert [item.name for item in items_by_category["pants"]] == ["Jeans"]


def test_cart_string_representation(base_cart: Cart):
    # then
    assert str(base_cart) == 'Cart has 3 products with $89.32'


def test_remove_last_item_from_empty_cart(empty_cart: Cart):
    # when && then
    with pytest.raises(EmptyCartError, match='Cannot remove item from empty cart'):
        empty_cart.remove_last_item()
