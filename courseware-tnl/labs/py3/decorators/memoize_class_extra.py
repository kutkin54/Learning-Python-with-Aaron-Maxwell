'''
>>> f(2)
CALLING: f 2
4
>>> f(2)
4
>>> f(7)
CALLING: f 7
49
>>> f(7)
49
>>> f(9)
CALLING: f 9
81
>>> f(9)
81
>>> f(7)
49
>>> f(2)
CALLING: f 2
4


>>> g(-6, 2)
CALLING: g -6 2
4
>>> g(-6, 2)
4
>>> g(-6, 2)
4
>>> g(6, 2)
CALLING: g 6 2
-2
>>> g(6, 2)
-2
>>> g(-6, 2)
4
>>> g(12, -2)
CALLING: g 12 -2
5
>>> g(12, -2)
5
>>> g(-6, 2)
4
>>> g(6, 2)
CALLING: g 6 2
-2


>>> h(2, 4)
CALLING: h 2 4 42
7
>>> h(2, 4)
7
>>> h(3, 2, z=31)
CALLING: h 3 2 31
6
>>> h(3, 2, z=31)
6
>>> h(2, 4)
7
>>> h(1, 1, z=-2)
CALLING: h 1 1 -2
-1
>>> h(3, 2, z=31)
CALLING: h 3 2 31
6

Let's ensure @Memoize is a class-based decorator, not function-based.
>>> type(Memoize)
<class 'type'>

'''
# Implement a memoize decorator that saves up to the two most recent
# calls.  (I.e., an LRU cache with max size of 2.)
# HINT: While not necessary, it may help to use the collections module.

# Write your code here:

from collections import OrderedDict


class Memoize:
    LIMIT = 2

    def __init__(self, func):
        self.func = func
        self.cache = OrderedDict()

    def __call__(self, *args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))
        if key in self.cache:
            self.cache.move_to_end(key)
        else:
            self.cache[key] = self.func(*args, **kwargs)
        if len(self.cache) > self.LIMIT:
            self.cache.popitem(False)
        assert len(self.cache) <= self.LIMIT, len(self.cache)

        return self.cache[key]


# Do not edit any code below this line!

@Memoize
def f(x):
    print("CALLING: f {}".format(x))
    return x ** 2


@Memoize
def g(x, y):
    print("CALLING: g {} {}".format(x, y))
    return (2 - x) // y


@Memoize
def h(x, y, z=42):
    print("CALLING: h {} {} {}".format(x, y, z))
    return z // (x + y)


if __name__ == '__main__':
    import doctest
    count, _ = doctest.testmod()
    if count == 0:
        print('*** ALL TESTS PASS ***\nGive someone a HIGH FIVE!')


# Copyright 2015-2018 Aaron Maxwell. All rights reserved.
