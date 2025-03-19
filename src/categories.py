from src.products import Product


class Category:
    """
    Класс для категорий товара
    """
    name: str
    description: str
    products: list

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1

    def add_product(self, product: Product):
        self.__products.append(product)
        Category.product_count = len(self.__products)

    @property
    def products(self):
        return self.__products

    @property
    def products_str(self):
        products_str = ""
        for product in self.__products:
            products_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return products_str
