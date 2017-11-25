class ListIterator(object):
    def __init__(self, array):
        self.array = array
        self.next_number = 0

    def __iter__(self):
        return self

    def __next__(self):
        number = self.next_number
        if self.next_number >= len(self.array):
            raise StopIteration()
        else:
            self.next_number += 1
            return self.array[number]

    next = __next__


#########
# Tests #
#########

import pytest

for elem in ListIterator([3, 2, 1]):
    print(elem)

def test_with_empty_list():
    it = iter(ListIterator([]))
    with pytest.raises(StopIteration):
        next(it)

def test_with_elements():
    it = iter(ListIterator(['a', 'b', 'c']))

    assert next(it) == 'a'
    assert next(it) == 'b'
    assert next(it) == 'c'

    with pytest.raises(StopIteration):
        next(it)