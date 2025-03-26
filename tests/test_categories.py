import pytest

from src.categories import Category
from src.products import Product
from src.categories import Smartphone
from src.categories import LawnGrass

# Тесты для класса Category
def test_category_initialization(sample_category):
    assert sample_category.name == "Категория1"
    assert sample_category.description == "Описание категории"
    assert len(sample_category.products) == 1
    assert sample_category.products[0].name == "Товар1"
    assert Category.product_count == 1


def test_category_str(sample_category):
    assert str(sample_category) == "Категория1, количество продуктов: 10 шт."


def test_category_add_product(sample_category, sample_smartphone):
    initial_product_count = len(sample_category.products)
    sample_category.add_product(sample_smartphone)
    assert len(sample_category.products) == initial_product_count + 1
    assert sample_category.products[-1].name == "Смартфон1"
    assert Category.product_count == initial_product_count + 1


def test_category_add_invalid_product(sample_category):
    with pytest.raises(TypeError, match="Можно добавить только объекты класса Product или его наследников"):
        sample_category.add_product("Некорректный продукт")


def test_category_products_info(sample_category):
    expected_info = "Товар1, 100 руб. Остаток: 10 шт.\n"
    assert sample_category.products_info == expected_info


# Тесты для класса Smartphone
def test_smartphone_initialization(sample_smartphone):
    assert sample_smartphone.name == "Смартфон1"
    assert sample_smartphone.efficiency == 90
    assert sample_smartphone.memory == 64
    assert sample_smartphone.color == "черный"


def test_smartphone_addition(sample_smartphone):
    other_smartphone = Smartphone("Смартфон2", "Описание смартфона", 6000, 3, 95, "Модель2", 128, "белый")
    total_price = (5 * 5000) + (3 * 6000)
    assert sample_smartphone + other_smartphone == total_price


def test_smartphone_add_invalid_type(sample_smartphone):
    with pytest.raises(TypeError):
        sample_smartphone + "Некорректный тип"


# Тесты для класса LawnGrass
def test_lawngras_initialization(sample_lawngras):
    assert sample_lawngras.name == "Травка1"
    assert sample_lawngras.country == "Россия"
    assert sample_lawngras.germination_period == 14
    assert sample_lawngras.color == "зеленый"


def test_lawngras_addition(sample_lawngras):
    other_lawngras = LawnGrass("Травка2", "Описание травы", 120, 15, "Беларусь", 12, "ярко-зеленый")
    total_price = (20 * 100) + (15 * 120)
    assert sample_lawngras + other_lawngras == total_price


def test_lawngras_add_invalid_type(sample_lawngras):
    with pytest.raises(TypeError):
        sample_lawngras + "Некорректный тип"