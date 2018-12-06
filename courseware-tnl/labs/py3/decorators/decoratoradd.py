def add(increment):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return increment + func(*args, **kwargs)
        return wrapper
    return decorator


def multiply(factor):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return factor * func(*args, **kwargs)
        return wrapper
    return decorator


@multiply(2)
@add(3)
def f(n):
    return n+2


print(f(4))
