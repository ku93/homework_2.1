from src.products import Product
from src.smartphone import Smartphone
from src.lawn_grass import LawnGrass


def test_print_mixin(capsys):
    Product("Samsung Galaxy S23 Ultra", "256 GB, Серый цвет, 200 MP камера", 180000.0, 5)
    message = capsys.readouterr()
    assert message.out == "Product(Samsung Galaxy S23 Ultra, 256 GB, Серый цвет, 200 MP камера, 180000.0, 5)\n"

    Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    message = capsys.readouterr()
    assert message.out == "Smartphone(Iphone 15, 512GB, Gray space, 210000.0, 8)\n"

    LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
    message = capsys.readouterr()
    assert message.out == "LawnGrass(Газонная трава 2, Выносливая трава, 450.0, 15)\n"
