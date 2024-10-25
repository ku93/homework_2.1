import pytest

from src.category import Category
from src.products import Product


@pytest.fixture
def product():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def category(product):
    return Category("Смартфоны", "Смартфоны, как средство не только коммуникации", [product])
