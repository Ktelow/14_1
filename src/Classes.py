from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный класс, определяющий общие свойства и методы классов"""

    @abstractmethod
    def __add__(self, other):
        pass


class MixinProduct:
    """Миксин для печати свойств продукта при его создании"""

    def __init__(self):
        print(repr(self))

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}',{self.description}, {self.price}, {self.quantity})"


class Product(MixinProduct, BaseProduct):
    """Класс для создания продуктов"""

    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Функция инизиализации продукта и его атрибутов"""
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        else:
            self.name = name
            self.description = description
            self.__price = price
            self.quantity = quantity
            super().__init__()

    @classmethod
    def new_product(cls, new_product):
        """Функция добавления нового продукта в класс"""
        return cls(
            name=new_product["name"],
            description=new_product["description"],
            price=new_product["price"],
            quantity=new_product["quantity"],
        )

    @property
    def price(self):
        """Функция для задачи цены"""
        return self.__price

    @price.setter
    def price(self, value):
        """Функция-сеттер для проверки положительна ли цена и установки её"""
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value

    def __str__(self):
        """Функция возврата строки с атрибутами продукта"""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Функция сложения продуктов одного класса"""
        if type(self) is type(other):
            return self.price * self.quantity + other.price * other.quantity
        else:
            raise TypeError


class Category:
    """Класс для создания категорий продуктов"""

    name: str
    description: str
    __products: list
    product_count = 0
    category_count = 0

    def __init__(self, name, description, products=None):
        """Функция инизиализации категории и её атрибутов"""
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    # def __str__(self):
    # for i in self.__products:
    # return f"{i["name"]}, {i["description"]}, {i["price"]}, {i["quantity"]}"

    def add_product(self, product):
        """Функция добавления продукта в категорию"""
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError

    @property
    def products(self):
        """Атрибут списка продуктов, выводящий список всех продуктов в объекте класса"""
        result = []
        for i in self.__products:
            result.append(str(i))
        return "\n".join(result)

    @products.setter
    def products(self, products):
        """Функция-сеттер для добавления продуктов"""
        name, descrpition, price, quantity = products[0], products[1], products[2], products[3]
        self.name = name
        self.description = descrpition
        self.price = price
        self.quantity = quantity

    def __str__(self):
        """Функция для возвращения общего количества продуктов в объекте класса"""
        quantity_summ = 0
        for i in self.__products:
            quantity_summ += i.quantity
        return f"{self.name}, количество продуктов: {quantity_summ} шт."

    def middle_price(self):
        price_sum = 0
        for i in self.__products:
            price_sum += i.price
        try:
            avg_price = price_sum / len(self.__products)
            return avg_price
        except ZeroDivisionError:
            return 0


class Smartphone(Product):
    """Дочерняя функция для создания продуктов-смартфонов"""

    efficiency = float
    model = str
    memory = int
    color = str

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        """Функция инизиализации смартфона и его атрибутов"""
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Дочерняя функция для создания продуктов-газонов"""

    country = str
    germination_period = str
    color = str

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        """Функция инизиализации газона и его атрибутов"""
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
