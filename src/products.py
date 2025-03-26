from abc import ABC, abstractmethod


class BaseProduct(ABC):
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self):
        pass

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price

    @classmethod
    def new_product(cls, prod):
        return cls(prod['name'], prod['description'], prod['price'], prod['quantity'])


class MixinLog:
    def __init__(self):
        print(repr(self))

    def __repr__(self):
        pass

class Product(BaseProduct, MixinLog):
    """
    Класс для описания товара в магазине
    """
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        MixinLog.__init__(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.description}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.name}, {self.price} руб. Остаток: {self.quantity} шт.'

    def __len__(self):
        return self.quantity

    def __add__(self, other):
        if type(other) is Product:
            return self.quantity * self.price + other.quantity * other.price
        raise TypeError

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price

    @classmethod
    def new_product(cls, prod):
        return cls(prod['name'], prod['description'], prod['price'], prod['quantity'])