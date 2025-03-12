class Product:
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, new_product):
        return cls(
            name=new_product["name"],
            description=new_product["description"],
            price=new_product["price"],
            quantity=new_product["quantity"],
        )

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        return self.price * self.quantity + other.price * other.quantity


class Category:
    name: str
    description: str
    __products: list
    product_count = 0
    category_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    # def __str__(self):
    # for i in self.__products:
    # return f"{i["name"]}, {i["description"]}, {i["price"]}, {i["quantity"]}"

    def add_product(self, product):
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        result = []
        for i in self.__products:
            result.append(str(i))
        return "\n".join(result)

    @products.setter
    def products(self, products):
        name, price, quantity = products[0], products[2], products[3]
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        quantity_summ = 0
        for i in self.__products:
            quantity_summ += i.quantity
        return f"{self.name}, количество продуктов: {quantity_summ} шт."
