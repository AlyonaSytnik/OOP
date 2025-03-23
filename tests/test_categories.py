import pytest
from src.categories import Category
from src.products import Product


def test_category_initialization(sample_category):
    assert sample_category.name == "Категория1"
    assert sample_category.description == "Описание категории"
    assert len(sample_category.products) == 1
    assert sample_category.products[0].name == "Товар1"


def test_category_str(sample_category):
    assert str(sample_category) == "Категория1, количество продуктов: 10 шт."


def test_add_product(sample_category):
    new_product = Product("Товар2", "Описание товара", 200, 5)
    sample_category.add_product(new_product)
    assert len(sample_category.products) == 2
    assert sample_category.products[-1].name == "Товар2"


def test_add_invalid_product(sample_category):
    with pytest.raises(TypeError, match="Добавляемый объект должен быть экземпляром класса Product или его наследников."):
        sample_category.add_product("Некорректный продукт")


def test_category_products_info(sample_category):
    expected_info = "Товар1, 100 руб. Остаток: 10 шт.\n"
    assert sample_category.products_info == expected_info


def test_category_product_count_increment(sample_category):
    initial_product_count = Category.product_count
    new_product = Product("Товар2", "Описание товара", 150, 5)
    sample_category.add_product(new_product)
    assert Category.product_count == initial_product_count + 1