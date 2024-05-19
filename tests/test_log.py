from src.decorators import log


def test_log_valid_data_with_file(tmp_path):
    """Тестирование записи в файл с переданным файлом."""

    @log(tmp_path / "my_log.txt")
    def func_with_file(x, y):
        return x + y

    result = func_with_file(3, 4)
    assert result == 7

    """Проверяем, что сообщение было записано в файл"""
    with open(tmp_path / "my_log.txt", "r") as f:
        assert f.read() == "my_function ok\n"


def test_log_valid_data_without_file(capsys):
    """Тестирование вывода в консоль без переданного файла."""

    @log()
    def func_without_file(x, y):
        return x + y

    result = func_without_file(1, 2)
    assert result == 3
    """Проверяем, что результат и сообщение "my_function ok" было выведено в консоль"""
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n\n"


def test_log_invalid_data_with_file(tmp_path):
    """Тестирование записи в файл с переданным файлом."""

    @log(tmp_path / "my_log.txt")
    def func_with_file(x, y):
        return x + y

    func_with_file(3, "a")

    """Проверяем, что сообщение было записано в файл"""
    with open(tmp_path / "my_log.txt", "r") as f:
        assert (
            f.read()
            == "my_function error: unsupported operand type(s) for +: 'int' and 'str'. Inputs: (3, 'a'), {}\n"
        )


def test_log_invalid_data_without_file(capsys):
    """Тестирование вывода в консоль без переданного файла."""

    @log()
    def func_without_file(x, y):
        return x + y

    func_without_file("$", 1)

    """Проверяем, что  сообщение  было выведено в консоль"""
    captured = capsys.readouterr()
    assert (
        captured.out
        == "my_function error: can only concatenate str (not \"int\") to str. Inputs: ('$', 1), {}\n\n"
    )
