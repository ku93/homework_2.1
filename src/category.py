from src.products import Product
from src.exceptions import ZerroQuantityProduct


class Category:
    """Класс для категорий"""

    # Атрибуты класса для хранения общей информации
    total_categories = 0  # Общее количество категорий
    total_products = 0  # Общее количество товаров

    def __init__(self, name: str, description: str, products=None):
        self.name = name  # Название категории
        self.description = description  # Описание категории
        self.__products = products if products is not None else []  # Список товаров категории
        Category.total_categories += 1  # Увеличиваем общее количество категорий
        Category.total_products += sum(product.quantity for product in self.__products)  # общее количество товаров

    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self.__products)} шт."

    def add_product(self, product):
        """Метод для добавления товара в категорию."""
        if isinstance(product, Product):
            self.__products.append(product)
            Category.total_products += product.quantity  # Увеличиваем общее количество товаров
            print(f"Добавлен {product.name} в категорию '{self.name}' (количество: {product.quantity}).")
        else:
            print("Ошибка: В объекте должен быть тип Product.")

    @property
    def products(self):
        products_str = ""
        for product in self.__products:
            products_str += f"{str(product)}\n"
        return products_str

    @products.setter
    def products(self, product: Product):
        if isinstance(product, Product):
            try:
                if product.quantity == 0:
                    raise ZerroQuantityProduct("Нельзя добавить продукт с нулевым количеством")
            except ZerroQuantityProduct as e:
                print(str(e))
            else:
                self.__products.append(product)
                Category.total_categories += 1
                print("Продукт добавлен успешно")
            finally:
                print("Обработка добавления продуктов завершена")
        else:
            raise TypeError

    @property
    def products_in_list(self):
        return self.__products

    def middle_price(self):
        try:
            return round(sum([product.price for product in self.__products]) / len(self.__products), 2)
        except ZeroDivisionError:
            return 0


if __name__ == "__main__":

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print(category1.name)
    print(category1.description)
    print(category1.products)
    print(category1.total_categories)
    print(category1.total_products)

    category2 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product4],
    )
    print(category2.name)
    print(category2.description)
    print(category2.products)
    print(category2.total_categories)
    print(category2.total_products)

    print(category2)

    print(category1.middle_price())

    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    print(category_empty.middle_price())
