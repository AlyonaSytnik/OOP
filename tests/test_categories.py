import pytest

from src.categories import Category
from src.products import Product
from src.categories import Smartphone
from src.categories import LawnGrass

def test_category_initialization():
    product1 = Product("Product 1", "Description 1", 100.0, 2)
    product2 = Product("Product 2", "Description 2", 150.0, 3)
    category = Category("Test Category", "Category Description", [product1, product2])

    assert category.name == "Test Category"
    assert category.description == "Category Description"
    assert len(category.products) == 2

def test_category_add_product():
    product1 = Product("Product 1", "Description 1", 100.0, 2)
    category = Category("Test Category", "Category Description", [product1])

    assert len(category.products) == 1

    product2 = Product("Product 2", "Description 2", 150.0, 3)
    category.add_product(product2)

    assert len(category.products) == 2

def test_category_add_product_type_error():
    category = Category("Test Category", "Category Description", [])

    with pytest.raises(TypeError):
        category.add_product("Not a Product")  # Добавляем строку вместо Product

    with pytest.raises(TypeError):
        category.add_product(123)  # Добавляем число вместо Product

def test_category_products_info():
    product1 = Product("Product 1", "Description 1", 100.0, 2)
    product2 = Product("Product 2", "Description 2", 150.0, 3)
    category = Category("Test Category", "Category Description", [product1, product2])

    expected_info = "Product 1, 100.0 руб. Остаток: 2 шт.\nProduct 2, 150.0 руб. Остаток: 3 шт.\n"
    assert category.products_info == expected_info

def test_smartphone_initialization():
    smartphone = Smartphone("Smartphone", "Smartphone description", 700.0, 5, 10, "Model X", 128, "Black")
    assert smartphone.name == "Smartphone"
    assert smartphone.efficiency == 10
    assert smartphone.model == "Model X"
    assert smartphone.memory == 128
    assert smartphone.color == "Black"

def test_smartphone_addition():
    smartphone1 = Smartphone("Smartphone 1", "Description", 700.0, 2, 10, "Model A", 64, "Blue")
    smartphone2 = Smartphone("Smartphone 2", "Description", 800.0, 1, 12, "Model B", 128, "Red")
    total_price = smartphone1 + smartphone2

    assert total_price == (2 * 700.0 + 1 * 800.0)

def test_lawn_grass_initialization():
    lawn_grass = LawnGrass("Lawn Grass", "Description", 50.0, 10, "USA", "30 days", "Green")
    assert lawn_grass.name == "Lawn Grass"
    assert lawn_grass.country == "USA"
    assert lawn_grass.germination_period == "30 days"

def test_lawn_grass_addition():
    grass1 = LawnGrass("Lawn Grass 1", "Description", 50.0, 3, "USA", "30 days", "Green")
    grass2 = LawnGrass("Lawn Grass 2", "Description", 60.0, 2, "Canada", "30 days", "Dark Green")
    total_price = grass1 + grass2

    assert total_price == (3 * 50.0 + 2 * 60.0)

def test_lawn_grass_repr_and_str():
    lawn_grass = LawnGrass("Lawn Grass", "Description", 50.0, 10, "USA", "30 days", "Green")
    assert repr(lawn_grass) == "LawnGrass('Lawn Grass', 'Description', 50.0, 10)"
    assert str(lawn_grass) == "Lawn Grass, 50.0 руб. Остаток: 10 шт."