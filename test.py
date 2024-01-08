def decorator_function(original_fn):
    def wrapper_function(*args, **kwargs):
        print('Text before result')

        result = original_fn(*args, **kwargs)

        print('Text after result')

        return result

    return wrapper_function


@decorator_function
def my_function(a, b):
    print('Test in my_function')

    return (a, b)


result = my_function(100, 50)
print(result)
