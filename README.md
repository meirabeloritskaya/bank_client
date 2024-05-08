# Проект card_client

## Описание:
Это веб-приложение на Python для управления задачами и проектами, которые показывает несколько последних успешных банковских операций клиента.

- реализована функция, которая принимает на вход номер карты и возвращает ее маску. Номер карты замаскирован и отображается в формате 
XXXX XX** **** XXXX
Т. е. видны первые 6 цифр и последние 4, номер разбит по блокам по 4 цифры, разделенным пробелами.

- реализована функция, которая принимает на вход номер счета и возвращает его маску. Номер счета замаскирован и отображается в формате
  **XXXX
  Т. е. видны только последние 4 цифры.

- реализована функция, которая принимать на вход строку с информацией — тип карты/счета и номер карты/счета.
Возвращать исходную строку с замаскированным номером карты/счета. Для карты и счета используйте разные маскировки.

- реализована  функция, которая принимает на вход строку вида 
2018-07-11T02:26:18.671407 и возвращает строку с датой в виде 
11.07.2018

- реализована функция, которая принимает на вход список словарей и значение для ключа state (опциональный параметр со значением по умолчанию 
EXECUTED) и возвращает новый список, содержащий только те словари, у которых ключ state содержит переданное в функцию значение.

 - реализована функция, которая принимает на вход список словарей и возвращает новый список, в котором исходные словари отсортированы по убыванию даты (ключ date).
    Функция принимает два аргумента, второй необязательный задает порядок сортировки (убывание, возрастание).


## Установка:

1. Клонируйте репозиторий:
```
git clone https://github.com/meirabeloritskaya/bank_client.git
```
2. Установите зависимости:
```
pip install -r requirements.txt
```


## Документация:
Для получения дополнительной информации обратитесь к [документации](docs/README.md).

## Лицензия:

Этот проект лицензирован по [лицензии MIT](LICENSE).

Для получения дополнительной информации обратитесь к [документации](docs/README.md).

## Лицензия:

Этот проект лицензирован по [лицензии MIT](LICENSE).
