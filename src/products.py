class Product:
    """Класс для продуктов"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name  # Название товара
        self.description = description  # Описание товара
        self.__price = price  # Цена товара
        self.quantity = quantity  # Количество в наличии

    @classmethod
    def new_product(cls, name, description, price, quantity):
        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price: str):
        if float(new_price) <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        self.__price = float(new_price)

    def __str__(self):
        return (
            f"Product(name={self.name}, description={self.description}, price={self.price}, quantity={self.quantity})"
        )


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    product1.price = "-1000"
    print(product1.price)
    product2.price = "1000"
    print(product2.price)
