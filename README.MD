# OOP_Project
##  Описание:
Проект в рамках выполнения домашних заданий в блоке ООП.
Созданы:
- класс представления продуктов с тестами;
- класс представления категорий продуктов с тестами;
- модуль по заполнению представителей классов данными из файла формата json;
- некоторые атрибуты разработанных классов сделаны приватными;
- добавлены сеттеры и геттеры для приватных атрибутов;
- добавлен запрос к пользователю на уменьшение цены;
- добавлен поиск аналогичных товаров в списке товаров в категории, при совпадении количество складывается, цена берётся большая;
- добавлен функционал в части складывания объектов товара;
- добавлен функционал в части строкового отображения;
- добавлен функционал в части перебора списка продуктов в объекте категории;
- добавлены наследники класса продуктов: smartphone, lawn_grass;
- внесена проверка на добавление 'не продуктов';
- внесена проверка на сложение товаров одного класса (телефон - телефон, трава - трава и т.д.);
- добавлен родительский абстрактный класс для продуктов;
- разработак миксин класс, выводящий в консоль при создании объекта информацию о нём;
- разработан абстрактный родительский класс для категории и заказа продуктов;
- разработан класс заказа продуктов (содержит один товар, его количество и итоговую цену);
- реализованы методы обработки исключений в случае создания товара с нулевым количеством;
- реализован метод подсчёта средней стоимости товаров с обработкой ошибки пустого списка товаров;
- тесты откорректированы в части нового функционала.
## Установка:
1. Клонируйте репозиторий:
```
git clone https://github.com/Aliniss/OOP.git
```
2. Установите зависимости:
```
pip install -r requirements.txt
```
## Использование:
Раздел будет дополняться по мере разработки.

## Тестирование
Набор тестов находится в пакете tests.

## Документация:
Для получения дополнительной информации обратитесь к [документации](docs/README.md).

## Лицензия:

Этот проект лицензирован по [лицензии MIT](LICENSE).