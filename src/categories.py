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
            raise TypeError("Можно добавить только объекты класса Product или его наследников (Smartphone/LawnGrass)")

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

    def middle_price(self):
        try:
            return sum([product.price for product in self.__products]) / len(self.__products)
        except ZeroDivisionError:
            return 0

class Smartphone(Product):
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        if type(other) is Smartphone:
            return self.quantity * self.price + other.quantity * other.price
        raise TypeError


class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        if type(other) is LawnGrass:
            return self.quantity * self.price + other.quantity * other.price
        raise TypeError