# Проект Homework_2

## Описание:

 Проект Homework_2 - это домашнее задание по ООП

## Установка:


1. Клонируйте репозиторий:
```chatinput
git clone git@github.com:ku93/homowork_2.git
```

2. Установите зависимости:
```chatinput
pip install -r requirements.txt
```

3. Проверьте домашнее задание.

## Функционал:

### Модули Product и Category

class Product - Класс для продуктов

class Category - Класс для категорий

__init__ - инициализирует класс

__str__ - превращает результат в строку

add_product - Метод для добавления товара в категорию

__len__ - Метод для возвращения количества продуктов в категории

get_product_count - Метод для получения общего количества продуктов в категории

### Модуль Product_iterator

Модуль итерации продуктов

### Модуль prod_json

Распределение информации по классам из JSON файла

### Модули smartphone и lawn_grass

Эти оба класса являются классами-наследниками от исходного класса 
Product

### Модуль base_product

 базовый абстрактный класс с именем 
BaseProduct
, который является родительским для класса продуктов

### Модуль print_mixin

Содержит класс-миксин, который при создании объекта, то есть при работе метода 
__init__
, печатать в консоль информацию о том, от какого класса и с какими параметрами был создан объект

## Тестирование

Для запуска тестов используйте: pytest

## Автор:
Ткачев Леонид Андреевич [e-mail] (tkachev1993adg@yandex.ru)

## Версия
от 05.11.2024 г.