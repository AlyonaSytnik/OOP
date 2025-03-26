import pytest

from src.categories import Category
from src.products import Product
from src.categories import Smartphone
from src.categories import LawnGrass

@pytest.fixture
def product():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера",180000.0,5)

@pytest.fixture
def first_category():
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        products=[
            Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
            Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
        ]
    )

@pytest.fixture
def second_category():
    return Category(
        name="Телевизоры",
        description="Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        products=[
            Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14),
            Product("55 QLED 4K", "Фоновая подсветка", 123000.0, 7)
        ]
    )


@pytest.fixture
def prod_data():
    prod_data = {
        'name': "Товар9",
        'description': "Описание товара",
        'price': 400,
        'quantity': 25
    }
    return prod_data


@pytest.fixture
def sample_product():
    return Product("Товар1", "Описание товара", 100, 10)


@pytest.fixture
def sample_smartphone():
    return Smartphone("Смартфон1", "Описание смартфона", 5000, 5, 90, "Модель1", 64, "черный")


@pytest.fixture
def sample_lawngras():
    return LawnGrass("Травка1", "Описание травы", 100, 20, "Россия", 14, "зеленый")


@pytest.fixture
def sample_category(sample_product):
    return Category("Категория1", "Описание категории", [sample_product])

@pytest.fixture(autouse=True)
def reset_category_counts():
    Category.category_count = 0
    Category.product_count = 0