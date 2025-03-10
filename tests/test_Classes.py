import pytest

from src.Classes import Category, Product


@pytest.fixture
def Product_Apple():
    return Product("Яблоко", "Сладкий фрукт", 10.0, 100)


@pytest.fixture()
def Category_Fruits():
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


def test_Product(Product_Apple):
    assert Product_Apple.name == "Яблоко"
    assert Product_Apple.description == "Сладкий фрукт"
    assert Product_Apple.price == 10.0
    assert Product_Apple.quantity == 100


def test_Category(Category_Fruits):
    assert Category_Fruits.name == "Фрукты"
    assert Category_Fruits.description == "Фрукты, растущие на дереве"
    assert Category_Fruits.product_count == 3
    assert Category_Fruits.category_count == 1


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


def test_category_init(Category_Fruits):
    """Тестирование корректности инициализации объектов класса Category"""
    assert Category_Fruits.name == "Фрукты"
    assert Category_Fruits.description == "Фрукты, растущие на дереве"

    """Тестирование корректности подсчета категорий и продуктов"""
    assert Category.category_count == 1
    assert Category.product_count == 3


def test_add_product(Category_Fruits):
    Category_Fruits.add_product(Product("морковь", "вкусная", 1, 50))
    assert Category_Fruits.product_count == 4


def test_price_setter(Product_Apple):
    carrot = Product("морковь", "вкусная", 1, 50)
    assert carrot.price == 1
    carrot.price = 0
    assert print(carrot.price) == None


def print_products(Category_fruits):
    printer = print(Category_fruits.products)
    assert printer == 0
