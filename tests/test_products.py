from src.products import Product

def test_product_init(product):
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5

def test_product_price_setter():
    """Тест для проверки установки цены."""
    product = Product("Товар 1", "Описание товара", 100, 10)
    product.price = 150
    assert product.price == 150

    product.price = -50  # Установка некорректной цены
    assert product.price == 150  # Цена не должна измениться
    product.price = 0  # Установка некорректной цены
    assert product.price == 150  # Цена не должна измениться

def test_product_price_error_message(capsys):
    """Тест для проверки сообщения об ошибке при установке некорректной цены."""
    product = Product("Товар 1", "Описание товара", 100, 10)
    product.price = -50
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out

def test_product_new_product(product_data, product):
    """Тест для проверки класса метода new_product."""
    product = Product.new_product(product_data)
    assert product.name == "Товар 2"
    assert product.description == "Описание товара 2"
    assert product.price == 200
    assert product.quantity == 5