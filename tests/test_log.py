from src.decorators import log, my_function


import pytest
import os


def test_log_valid_data_with_file(capsys):
    """Тестирование записи в файл с переданным файлом."""

    @log("my_log.txt")
    def decorated_function():
        return my_function(3, 4)

    result = decorated_function()
    assert result == 7
    """Проверяем, что результат был выведен в консоль"""
    captured = capsys.readouterr()
    assert captured.out == "7\n"
    """Проверяем, что сообщение было записано в файл"""
    with open("my_log.txt", "r") as f:
        assert f.read() == "my_function ok\n"


def test_log_valid_data_without_file(capsys):
    """Тестирование вывода в консоль без переданного файла."""

    @log()
    def decorated_function():
        return my_function(1, 2)

    result = decorated_function()
    assert result == 3
    """Проверяем, что результат и сообщение "my_function ok" было выведено в консоль"""
    captured = capsys.readouterr()
    assert captured.out == "3\nmy_function ok\n"


def test_log_invalid_data_with_file(capsys):
    """Тестирование записи в файл с переданным файлом."""

    @log("my_log.txt")
    def decorated_function():
        return my_function("a", 4)

    with pytest.raises(Exception):
        decorated_function()
    assert os.path.exists("my_log.txt")

    """Проверяем, что сообщение было записано в файл"""
    with open("my_log.txt", "r") as f:
        assert "my_function error" in f.read()


def test_log_invalid_data_without_file(capsys):
    """Тестирование вывода в консоль без переданного файла."""

    @log()
    def decorated_function():
        return my_function(1, "$")

    with pytest.raises(Exception):
        decorated_function()

    """Проверяем, что  сообщение  было выведено в консоль"""
    captured = capsys.readouterr()
    assert "my_function error" in captured.out
