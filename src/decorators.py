from functools import wraps


def log(filename=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            """декоратор log будет логировать вызов функции и ее результат в файл или в консоль"""
            try:
                result = func(*args, **kwargs)
                my_message = "my_function ok\n"
                if filename:
                    with open(filename, "a") as f:
                        f.write(my_message)
                else:
                    print(my_message)
                return result

            except Exception as e:
                error_message = f"my_function error: {e}. Inputs: {args}, {kwargs}\n"
                if filename:
                    with open(filename, "a") as f:
                        f.write(error_message)
                else:
                    print(error_message)
                return error_message

        return wrapper

    return decorator


# валидные данные, результат записан в файл
@log(filename="my_log.txt")
def my_function(x, y):
    return x + y


print(my_function(1, 2))
# валидные данные, результат записан в консоль
# @log()
# def my_function(x, y):
#     return x + y
#
# print(my_function(1, 2))

# инвалидные данные, результат записан в файл
# @log(filename="my_log.txt")
# def my_function(x, y):
#     return x + y
#
# my_function('a', 2)

# инвалидные данные, результат записан в консоль
# @log()
# def my_function(x, y):
#     return x + y
#
# my_function("a", 2)
