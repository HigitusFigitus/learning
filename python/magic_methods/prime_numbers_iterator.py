from math import sqrt
from itertools import count, islice

class PrimeNumbersIterator(object):
    def __init__(self):
        self.next_number = 2

    def __iter__(self):
        return self

    def _is_prime(self, n):
        return all(n%i for i in islice(count(2), int(sqrt(n)-1)))

    def __next__(self):
        number = self.next_number
        while not self._is_prime(number):
            number += 1
        self.next_number = number + 1
        return number

    next = __next__


#########
# Tests #
#########

def test_prime_numbers():
    iterator = iter(PrimeNumbersIterator())

    assert next(iterator) == 2
    assert next(iterator) == 3
    assert next(iterator) == 5
    assert next(iterator) == 7
    assert next(iterator) == 11
    assert next(iterator) == 13
    assert next(iterator) == 17
    assert next(iterator) == 19
    assert next(iterator) == 23
    assert next(iterator) == 29
    assert next(iterator) == 31
    assert next(iterator) == 37

def test_is_prime():
    obj = PrimeNumbersIterator()
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for number in prime_numbers:
        assert obj._is_prime(number) is True, "{} should be prime".format(number)

    not_prime_numbers = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 24, 25, 26]

    for number in not_prime_numbers:
        assert obj._is_prime(number) is False, "{} should NOT be prime".format(number)

