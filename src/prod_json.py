import json
import os

from src.category import Category
from src.products import Product


def read_json(path: str) -> dict:
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="utf-8") as file:
        data = json.load(file)
        return data


def create_objects_from_json(data):
    category = []
    for categor in data:
        products = []
        for product in categor["products"]:
            products.append(Product(**product))
        categor["products"] = products
        category.append(Category(**categor))
    return category


if __name__ == "__main__":
    raw_data = read_json("../data/products.json")
    category_data = create_objects_from_json(raw_data)
    print(category_data)
