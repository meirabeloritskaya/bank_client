def log(filename=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                my_messege = "my_function ok\n"
                if filename:
                    with open(filename, "a") as f:
                        f.write(my_messege)
                else:
                    print(my_messege)
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


@log(filename="my_log.txt")
def my_function(x, y):
    return x + y


print(my_function(1, 2))

# @log()
# def my_function(x, y):
#     return x + y
#
# print(my_function(1, 2))


# @log(filename="my_log.txt")
# def my_function(x, y):
#     return x + y
#
# my_function('a', 2)

# @log()
# def my_function(x, y):
#     return x + y
#
# my_function("a", 2)
