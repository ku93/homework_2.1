class Product:
    """Класс для продуктов"""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name  # Название товара
        self.description = description  # Описание товара
        self.__price = price  # Цена товара
        self.quantity = quantity  # Количество в наличии

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Складывает полные цены двух продуктов."""
        if type(other) is Product:
            return self.full_price + other.full_price
        raise TypeError("Операция сложения поддерживается только для объектов Product.")

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_price: float):
        if new_price <= 0:
            raise ValueError("Цена не должна быть нулевая или отрицательная")
        self.__price = new_price

    @property
    def full_price(self) -> float:
        """Возвращает полную цену на основе количества."""
        return self.__price * self.quantity

    @full_price.setter
    def full_price(self, new_full_price: float):
        if new_full_price > 0:
            self.quantity = new_full_price / self.__price
        else:
            raise ValueError("Полная цена товара не может быть отрицательной.")

if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)

    print(product1)
    print(product2)
    print(product3)

    try:
        product1.price = -1000  # Пример неправильного присвоения
    except ValueError as e:
        print(e)

    product2.price = 1000  # Пример правильного присвоения
    print(product2.price)

    print(f"Сумма полных цен: {product1 + product2}")  # Сложение полных цен
