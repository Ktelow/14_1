import pytest

from src.Classes import Category, Product


@pytest.fixture
def Product_Apple():
    return Product("Яблоко", "Сладкий фрукт", 10.0, 100)


@pytest.fixture()
def Category_Fruits():
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
