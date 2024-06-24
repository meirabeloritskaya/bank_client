# Проект card_client

## Описание:

- реализована функция, которая принимает на вход список словарей и значение для ключа 
state (опциональный параметр со значением по умолчанию EXECUTED)

и возвращает новый список, содержащий только те словари, у которых ключ state
 содержит переданное в функцию значение.

- реализована функцию, которая принимает на вход список словарей и возвращает новый список, в котором исходные словари отсортированы по убыванию даты (ключ 
date). Функция принимает два аргумента, второй необязательный задает порядок сортировки (убывание, возрастание).

- реализована функцию, которая принимает список словарей с банковскими операциями (или объект-генератор, который выдает по одной банковской операции)
   и возвращает итератор, который выдает по очереди операции, в которых указана заданная валюта.
  
- реализован генератор, который принимает список словарей и возвращает описание каждой операции по очереди
  
- реализован генератор номеров банковских карт, который должен генерировать номера карт в формате 
XXXX XXXX XXXX XXXX, где X — цифра. Должны быть сгенерированы номера карт в заданном диапазоне, например от 0000 0000 0000 0001 до 9999 9999 9999 9999 (диапазоны передаются как параметры генератора).


## Установка:

1. Клонируйте репозиторий:
```
git clone https://github.com/meirabeloritskaya/bank_client.git
```
2. Установите зависимости:
```
pip install -r requirements.txt
```

## Тестирование:

- реализованы тестовые функции с использованием библиотеки pytest для существующего кода проекта.
- Использованы фикстуры для формирования входных данных для тестов.
- Использована параметризация в тестах для запуска одного теста с различным набором входных параметров.
- покрытие тестами 100%



## Документация:

Для получения дополнительной информации обратитесь к [документации](docs/README.md).

## Лицензия:

Этот проект лицензирован по [лицензии MIT](LICENSE).


## Лицензия:

Этот проект лицензирован по [лицензии MIT](LICENSE).
