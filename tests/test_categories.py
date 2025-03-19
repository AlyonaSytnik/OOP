from src.categories import Category
from src.products import Product


def test_category_initialization():
    """Тест для проверки инициализации категории."""
    category = Category("Электроника", "Все виды электроники", [])
    assert category.name == "Электроника"
    assert category.description == "Все виды электроники"
    assert category.products == []  # Убедитесь, что продуктов еще нет
    assert Category.category_count == 1  # Счетчик категорий должен увеличиться


def test_add_product():
    """Тест для проверки добавления продукта в категорию."""
    category = Category("Электроника", "Все виды электроники", [])
    product = Product("Смартфон", "Современный смартфон", 50000, 30)

    category.add_product(product)
    assert len(category.products) == 1  # Продукт должен быть добавлен
    assert category.products[0] == product  # Убедитесь, что добавленный продукт правильный
    assert Category.product_count == 1  # Счетчик продуктов должен увеличиться


def test_add_multiple_products(second_category):
    """Тест для проверки добавления нескольких продуктов."""
    product1 = Product("Смартфон", "Современный смартфон", 50000, 30)
    product2 = Product("Ноутбук", "Мощный ноутбук", 80000, 15)

    second_category.add_product(product1)
    second_category.add_product(product2)

    assert second_category.products[2] == product1
    assert second_category.products[3] == product2
    assert second_category.product_count == 4  # Счетчик продуктов должен увеличиться


def test_products_str():
    """Тест для проверки формата строки продуктов."""
    category = Category("Электроника", "Все виды электроники", [])
    product1 = Product("Смартфон", "Современный смартфон", 50000, 30)
    product2 = Product("Ноутбук", "Мощный ноутбук", 80000, 15)

    category.add_product(product1)
    category.add_product(product2)

    expected_output = (
        "Смартфон, 50000 руб. Остаток: 30 шт.\n"
        "Ноутбук, 80000 руб. Остаток: 15 шт.\n"
    )
    assert category.products_str == expected_output