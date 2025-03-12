import pytest

from src.Classes import Category, Product


@pytest.fixture
def product_apple():
    return Product("Яблоко", "Сладкий фрукт", 10.0, 100)


@pytest.fixture
def product_carrot():
    return Product("Морковь", "Оранжевая", 20, 10)


@pytest.fixture()
def category_fruits():
    Category.category_count = 0
    Category.product_count = 0
    return Category(
        "Фрукты",
        "Фрукты, растущие на дереве",
        [
            Product("Персик", "Сочный", 5.0, 15),
            Product("Яблоко", "Сладкое", 6.0, 10),
            Product("Груша", "Нельзя скушать", 4, 20),
        ],
    )


def test_Product(product_apple):
    assert product_apple.name == "Яблоко"
    assert product_apple.description == "Сладкий фрукт"
    assert product_apple.price == 10.0
    assert product_apple.quantity == 100


def test_Category(category_fruits):
    assert category_fruits.name == "Фрукты"
    assert category_fruits.description == "Фрукты, растущие на дереве"
    assert category_fruits.product_count == 3
    assert category_fruits.category_count == 1


# @pytest.fixture()
# def Category_Veggies():
# yield Category(
# "Овощи",
# "Вкусные овощи",
# [
#    Product("Помидор", "Сочный", 5.0, 15),
#    Product("Картофель", "Сладкий", 6.0, 10),
#    Product("Капуста", "Многослойная", 4, 20),
# ],
# )


def test_category_init(category_fruits):
    """Тестирование корректности инициализации объектов класса Category"""
    assert category_fruits.name == "Фрукты"
    assert category_fruits.description == "Фрукты, растущие на дереве"

    """Тестирование корректности подсчета категорий и продуктов"""
    assert Category.category_count == 1
    assert Category.product_count == 3


def test_add_product(category_fruits):
    category_fruits.add_product(Product("морковь", "вкусная", 1, 50))
    assert category_fruits.product_count == 4


def test_price_setter(product_apple):
    carrot = Product("морковь", "вкусная", 1, 50)
    assert carrot.price == 1
    carrot.price = 0
    assert print(carrot.price) == None


def print_products(category_fruits):
    printer = print(category_fruits.products)
    assert printer == 0


def test_add(product_apple, product_carrot):
    assert product_apple + product_carrot == 1200


def test_str(category_fruits, product_carrot):
    assert str(category_fruits) == "Фрукты, количество продуктов: 45 шт."
    assert str(product_carrot) == "Морковь, 20 руб. Остаток: 10 шт."
