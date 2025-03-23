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
        Category.product_count += len(products)

    def __str__(self):
        prod_quantity = 0
        for product in self.__products:
            prod_quantity += product.quantity
        return f'{self.name}, количество продуктов: {prod_quantity} шт.'

    def add_product(self, product: Product):
        if not isinstance(product, Product):
            raise TypeError("Добавляемый объект должен быть экземпляром класса Product или его наследников.")

        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        return self.__products

    @property
    def products_info(self):
        products_info = ""
        for product in self.__products:
            products_info += str(product) + "\n"
        return products_info
