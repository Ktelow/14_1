import pytest

from src.Classes import Category, Product, Smartphone, LawnGrass


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


@pytest.fixture()
def product_smartphone():
    return Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )


@pytest.fixture()
def product_lawn():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


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


def test_smartphone(product_smartphone):
    assert product_smartphone.name == "Samsung Galaxy S23 Ultra"
    assert product_smartphone.description == "256GB, Серый цвет, 200MP камера"
    assert product_smartphone.price == 180000.0
    assert product_smartphone.quantity == 5
    assert product_smartphone.efficiency == 95.5
    assert product_smartphone.model == "S23 Ultra"
    assert product_smartphone.memory == 256
    assert product_smartphone.color == "Серый"


def test_lawn(product_lawn):
    assert product_lawn.name == "Газонная трава"
    assert product_lawn.description == "Элитная трава для газона"
    assert product_lawn.price == 500.0
    assert product_lawn.quantity == 20
    assert product_lawn.country == "Россия"
    assert product_lawn.germination_period == "7 дней"
    assert product_lawn.color == "Зеленый"


def test_add_error(product_lawn, product_smartphone):
    with pytest.raises(TypeError):
        print(product_smartphone + product_lawn)
