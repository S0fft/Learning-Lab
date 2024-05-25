from functools import wraps


def outer(a=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)

            return result

        return wrapper

    return decorator


@decorator(123)
def some():
    pass


def new():
    pass


new = decorator(new)
