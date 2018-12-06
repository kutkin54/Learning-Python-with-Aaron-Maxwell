def printlog(func):
    def wrapper(arg):
        print("CALLING: " + func.__name__)
        return func(arg)
    return wrapper


@printlog
def f(n):
    return n + 2


@printlog
def f2(n):
    return n * n


@printlog
def f3():
    print('hola')


print(f(3))

print(f2(3))
print(f3())
