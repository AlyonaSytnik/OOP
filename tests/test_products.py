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
    total_price = (5 * 100) + (10 * 200)
    assert product1 + product2 == total_price


def test_product_addition_invalid_type():
    product1 = Product("Товар6", "Описание товара", 150, 3)
    with pytest.raises(TypeError):
        product1 + "Некорректный тип"


def test_product_price_setter_valid():
    product = Product("Товар7", "Описание товара", 250, 15)
    product.price = 300
    assert product.price == 300


def test_product_price_setter_invalid():
    product = Product("Товар8", "Описание товара", 250, 15)
    product.price = -50  # Устанавливаем некорректную цену
    assert product.price == 250  # Цена должна остаться 250, так как установка была некорректной


def test_product_new_product():
    product_data = {
        'name': "Товар9",
        'description': "Описание товара",
        'price': 400,
        'quantity': 25
    }
    product = Product.new_product(product_data)
    assert product.name == "Товар9"
    assert product.description == "Описание товара"
    assert product.price == 400
    assert product.quantity == 25