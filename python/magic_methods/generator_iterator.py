##################
# With generator #
#################

def custom_range(start, end, step=1):
    while start < end:
        yield start
        start += step
    raise StopIteration()

##################
# With iterator #
#################

class RangeIterable(object):
    def __init__(self, start, end, step):
        self.start = start
        self.end = end
        self.step = step

    def __next__(self):
        number = self.start
        if self.start >= self.end:
            raise StopIteration()
        else:
            self.start += self.step
            return number

    next = __next__


class RangeIterator(object):
    def __init__(self, start, end, step=1):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        return RangeIterable(self.start, self.end, self.step)


#########
# Tests #
#########

import pytest

# custom_range = RangeIterator

def test_with_step():
    gen1 = iter(custom_range(2, 10, 2))
    assert next(gen1) == 2
    assert next(gen1) == 4
    assert next(gen1) == 6
    assert next(gen1) == 8
    with pytest.raises(StopIteration):
        next(gen1)

def test_starting_from_zero():
    gen1 = iter(custom_range(0, 3))
    assert next(gen1) == 0
    assert next(gen1) == 1
    assert next(gen1) == 2
    with pytest.raises(StopIteration):
        next(gen1)

def test_starting_over_zero():
    gen1 = iter(custom_range(3, 6))
    assert next(gen1) == 3
    assert next(gen1) == 4
    assert next(gen1) == 5
    with pytest.raises(StopIteration):
        next(gen1)
