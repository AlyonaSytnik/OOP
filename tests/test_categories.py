import pytest
from src.categories import Category, Smartphone, LawnGrass
from src.products import Product

def test_category_initialization():
    product1 = Product("Товар1", "Описание1", 100, 10)
    product2 = Product("Товар2", "Описание2", 200, 5)
    category = Category("Категория1", "Описание категории", [product1, product2])
    assert category.name == "Категория1"
    assert category.description == "Описание категории"
    assert len(category.products) == 2

def test_category_add_product():
    product = Product("Товар", "Описание", 100, 10)
    category = Category("Категория", "Описание", [])
    category.add_product(product)
    assert len(category.products) == 1

def test_category_add_invalid_product():
    category = Category("Категория", "Описание", [])
    with pytest.raises(TypeError):
        category.add_product("Некорректный продукт")

def test_category_middle_price():
    product1 = Product("Товар1", "Описание1", 100, 10)
    product2 = Product("Товар2", "Описание2", 200, 5)
    category = Category("Категория", "Описание", [product1, product2])
    assert category.middle_price() == (100 + 200) / 2

def test_category_middle_price_zero_products():
    category = Category("Категория", "Описание", [])
    assert category.middle_price() == 0

# Тесты для Smartphone
def test_smartphone_initialization():
    smartphone = Smartphone("Смартфон", "Описание", 30000, 15, "Высокая", "Модель1", "64GB", "Черный")
    assert smartphone.name == "Смартфон"
    assert smartphone.efficiency == "Высокая"

def test_smartphone_addition():
    smartphone1 = Smartphone("Смартфон1", "Описание1", 30000, 15, "Высокая", "Модель1", "64GB", "Черный")
    smartphone2 = Smartphone("Смартфон2", "Описание2", 40000, 10, "Средняя", "Модель2", "128GB", "Синий")
    assert smartphone1 + smartphone2 == 850000  # 15*30000 + 10*40000

# Тесты для LawnGrass
def test_lawngras_initialization():
    lawn_grass = LawnGrass("Газон", "Описание", 1500, 20, "Россия", "2 недели", "Зеленый")
    assert lawn_grass.name == "Газон"
    assert lawn_grass.country == "Россия"

def test_lawngras_addition():
    lawn_grass1 = LawnGrass("Газон1", "Описание", 1500, 20, "Россия", "2 недели", "Зеленый")
    lawn_grass2 = LawnGrass("Газон2", "Описание", 1600, 10, "Франция", "3 недели", "Синий")
    assert lawn_grass1 + lawn_grass2 == 46000  # 20 * 1500 + 10 * 1600