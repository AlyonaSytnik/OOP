import pytest
from src.products import Product

def test_product_initialization():
    product = Product("Товар1", "Описание товара", 100, 50)
    assert product.name == "Товар1"
    assert product.description == "Описание товара"
    assert product.price == 100
    assert product.quantity == 50


def test_product_str():
    product = Product("Товар2", "Описание товара", 200, 10)
    assert str(product) == "Товар2, 200 руб. Остаток: 10 шт."


def test_product_len():
    product = Product("Товар3", "Описание товара", 300, 20)
    assert len(product) == 20


def test_product_addition():
    product1 = Product("Товар4", "Описание товара", 100, 5)
    product2 = Product("Товар5", "Описание товара", 200, 10)
    assert product1 + product2 == (5 * 100) + (10 * 200)


def test_product_price_setter():
    product = Product("Товар6", "Описание товара", 150, 25)
    product.price = 200
    assert product.price == 200
    product.price = -50
    assert product.price == 200  # Должно остаться 200, так как цена была некорректной


def test_product_new_product(prod_data, product):
    product = Product.new_product(prod_data)
    assert product.name == "Товар7"
    assert product.description == "Описание товара"
    assert product.price == 250
    assert product.quantity == 30