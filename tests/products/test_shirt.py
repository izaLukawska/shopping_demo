import pytest

from shopping.products import Shirt, Category


@pytest.fixture
def v_neck() -> Shirt:
    return Shirt('V-Neck', 12.56)


def test_shirt_initialization_and_properties(v_neck: Shirt):
    # then
    assert v_neck.category == Category.SHIRT
    assert v_neck.name == 'V-Neck'
    assert v_neck.price == 12.56


def test_shirt_description(v_neck: Shirt):
    # then
    assert v_neck.description() == 'Shirt: V-Neck'


def test_shirt_name(v_neck: Shirt):
    # then
    assert v_neck.name == 'V-Neck'


def test_shirt_price(v_neck: Shirt):
    # then
    assert v_neck.price == 12.56


def test_shirt_price_update(v_neck: Shirt):
    # when
    v_neck.price = 11.00

    # then
    assert v_neck.price == 11.00


def test_shirt_category(v_neck: Shirt):
    # then
    assert v_neck.category == Category.SHIRT


def test_price_cannot_be_negative(v_neck: Shirt):
    # when && then
    with pytest.raises(ValueError, match='Price cannot be negative'):
        v_neck.price = -10.00


def test_shirt_representation(v_neck: Shirt):
    # then
    assert repr(v_neck) == "'V-Neck', $12.56"


def test_shirt_string_representation(v_neck: Shirt):
    # then
    assert str(v_neck) == 'SHIRT V-Neck has price $12.56'
