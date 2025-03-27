import pytest
from src.products import Product, BaseProduct


def test_base_product_initialization():
    product = Product("Товар", "Описание", 100, 10)
    assert product.name == "Товар"
    assert product.description == "Описание"
    assert product.price == 100
    assert product.quantity == 10

def test_product_price_setter():
    product = Product("Товар", "Описание", 100, 10)
    product.price = 200
    assert product.price == 200

def test_product_price_setter_negative():
    product = Product("Товар", "Описание", 100, 10)
    product.price = -50
    assert product.price == 100  # Цена не должна измениться на отрицательную

def test_product_repr():
    product = Product("Товар", "Описание", 100, 10)
    assert repr(product) == "Product('Товар', 'Описание', 100, 10)"

def test_product_str():
    product = Product("Товар", "Описание", 100, 10)
    assert str(product) == "Товар, 100 руб. Остаток: 10 шт."

def test_product_length():
    product = Product("Товар", "Описание", 100, 10)
    assert len(product) == 10

def test_product_addition():
    product1 = Product("Товар1", "Описание1", 100, 10)  # 1000
    product2 = Product("Товар2", "Описание2", 200, 5)    # 1000
    assert product1 + product2 == 2000  # 1000 + 1000 = 2000

def test_product_zero_quantity():
    with pytest.raises(ValueError):
        Product("Товар", "Описание", 100, 0)
