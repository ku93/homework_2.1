import pytest
from pyexpat.errors import messages

from src.exceptions import ZerroQuantityProduct
from src.products import Product


def test_category_init(category):
    assert category.name == "Смартфоны"
    assert category.description == "Смартфоны, как средство не только коммуникации"
    assert len(category.products_in_list) == 1


def test_add_product_and_count(category, product):
    """Тест на добавление продукта в категорию и подсчет продуктов."""
    # Убедимся, что в начале в категории только один продукт
    assert len(category.products_in_list) == 1  # Добавляем новый продукт
    new_product = product
    category.add_product(new_product)  # Добавляем новый продукт # Проверяем, что теперь в категории 2 продукта
    assert len(category.products_in_list) == 2


def test_total_products(category):
    """Тест на общее количество продуктов в категории."""
    assert len(category.products_in_list) == 1  # Проверяем, что в категории 1 продукт


def test_category_property(category):
    assert category.products == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"


def test_category_setter(category, product):
    assert len(category.products_in_list) == 1
    category.products = product
    assert len(category.products_in_list) == 2


def test_category_str(category):
    assert str(category) == "Смартфоны, количество продуктов: 1 шт."


def test_product_iterator(product_iterator):
    iter(product_iterator)
    assert product_iterator.index == 0
    assert next(product_iterator).name == "Samsung Galaxy S23 Ultra"

    with pytest.raises(StopIteration):
        next(product_iterator)


def test_category_setter_error(category, product):
    with pytest.raises(TypeError):
        category.products = 1


def test_category_setter_smartphone(category, smartphone1):
    category.products = smartphone1


def test_middle_price(category, empty_category):
    assert category.middle_price() == 180000.0
    assert empty_category.middle_price() == 0


def test_custom_exception(capsys, category, product):
    assert len(category.products_in_list) == 1

    with pytest.raises(ValueError) as e_info:
        prod_add = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 0)
        assert prod_add == "Товар с нулевым количеством не может быть добавлен"

    product.quantity = 0
    category.products = product
    message = capsys.readouterr()
    parts = message.out.split("\n")
    assert parts[1] == "Нельзя добавить продукт с нулевым количеством"
    assert parts[2] == "Обработка добавления продуктов завершена"
