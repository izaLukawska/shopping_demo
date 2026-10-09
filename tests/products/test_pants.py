import pytest

from shopping.products import Pants, Category


@pytest.fixture
def jeans() -> Pants:
    return Pants('Jeans', 34.00)

def test_pants_initialization_and_properties(jeans: Pants):
    #then
    assert jeans.category == Category.PANTS
    assert jeans.name == 'Jeans'
    assert jeans.price == 34.00

def test_pants_description(jeans:Pants):
    #then
    assert jeans.description() == 'Pants: Jeans'
