'''

Let's write a couple of trickier functions, which scan through
passed-in keyword arguments.

>>> country_populations = {
...     "Russia": 144,
...     "USA": 319,
...     "Philippines": 99,
...     "India": 1252,
... }

>>> val_for_longest_key(a=1)
1
>>> val_for_longest_key(a=2, aa=3)
3
>>> val_for_longest_key(foo=10, alpha=3, x=9)
3
>>> val_for_longest_key(**country_populations)
99

>>> key_for_biggest_value(a=1)
'a'
>>> key_for_biggest_value(a=2, aa=3)
'aa'
>>> key_for_biggest_value(foo=10, alpha=3, x=9)
'foo'
>>> key_for_biggest_value(**country_populations)
'India'

'''
import math
# Write your code here:


def val_for_longest_key(**kwargs):
    longest_key = 0
    val_for_longest_key = None
    for k, v in kwargs.items():
        if longest_key < len(k):
            val_for_longest_key = v
            longest_key = len(k)
    return val_for_longest_key


def key_for_biggest_value(**kwargs):
    longest_value = 0
    key_for_biggest_value = None
    for k, v in kwargs.items():
        if longest_value < v:
            key_for_biggest_value = k
            longest_value = v
    return key_for_biggest_value
# Do not edit any code below this line!


if __name__ == '__main__':
    import doctest
    count, _ = doctest.testmod()
    if count == 0:
        print('*** ALL TESTS PASS ***\nGive someone a HIGH FIVE!')

# Copyright 2015-2018 Aaron Maxwell. All rights reserved.
