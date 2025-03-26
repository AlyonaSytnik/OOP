import pytest
from src.products import Product


def test_product_initialization():
    product = Product("Test Product", "Description", 100.0, 10)
    assert product.name == "Test Product"
    assert product.description == "Description"
    assert product.price == 100.0
    assert product.quantity == 10


def test_product_price_setter():
    product = Product("Test Product", "Description", 100.0, 10)

    # Проверяем установку положительной цены
    product.price = 200.0
    assert product.price == 200.0

    # Проверяем недопустимую цену
    product.price = -50.0
    assert product.price == 200.0  # Цена не должна измениться

    # Проверка установки нулевой цены
    product.price = 0.0
    assert product.price == 200.0  # Цена также не должна измениться


def test_product_repr_and_str():
    product = Product("Test Product", "Description", 100.0, 10)
    assert repr(product) == "Product('Test Product', 'Description', 100.0, 10)"
    assert str(product) == "Test Product, 100.0 руб. Остаток: 10 шт."


def test_product_addition():
    product1 = Product("Product 1", "Description 1", 100.0, 2)
    product2 = Product("Product 2", "Description 2", 150.0, 3)
    total_price = product1 + product2

    assert total_price == (2 * 100.0 + 3 * 150.0)