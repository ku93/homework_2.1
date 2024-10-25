from src.products import Product


def test_product_init(product):
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_product_creat():
    product = Product("Samsung", "Серый цвет", 180000.0, 5)
    assert product.name == "Samsung"
    assert product.description == "Серый цвет"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_product_upgread(capsys, product):
    product.price = "-1000"
    messege = capsys.readouterr()
    assert messege.out.strip() == "Цена не должна быть нулевая или отрицательная"
    assert product.price == 180000.0
    product.price = 1000
    assert product.price == 1000
