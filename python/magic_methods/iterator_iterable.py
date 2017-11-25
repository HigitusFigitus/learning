class ListIterable(object):
    def __init__(self, array):
        self.array = array
        self.next_number = 0

    def __next__(self):
        number = self.next_number
        if self.next_number >= len(self.array):
            raise StopIteration()
        else:
            self.next_number += 1
            return self.array[number]
    
    next = __next__


class ListIterator(object):
    def __init__(self, array):
        self.array = array

    def __iter__(self):
        return ListIterable(self.array)


#########
# Tests #
#########

import pytest

iterator = ListIterator([3, 2, 1])
for elem in iterator:
    print(elem)
print("====================")
for elem in iterator:
    print(elem)


def test_with_empty_list():
    iterator = ListIterator([])
    it = iter(iterator)
    with pytest.raises(StopIteration):
        next(it)

    it = iter(iterator)
    with pytest.raises(StopIteration):
        next(it)

def test_with_elements():
    iterator = ListIterator(['a', 'b', 'c'])
    it = iter(iterator)

    assert next(it) == 'a'
    assert next(it) == 'b'
    assert next(it) == 'c'

    with pytest.raises(StopIteration):
        next(it)

    it = iter(iterator)

    assert next(it) == 'a'
    assert next(it) == 'b'
    assert next(it) == 'c'

