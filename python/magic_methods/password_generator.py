import string
import random

class SimplePasswordGenerator(object):
    def __init__(self, available_chars=None, length=8):
        if not available_chars:
            available_chars = list(string.ascii_lowercase + 
                                   string.digits +
                                   string.punctuation)
        self.available_chars = available_chars
        self.length = length

    def __iter__(self):
        return self

    def next(self):  # use __next__ in Python 3.x
        pw = ''
        for i in range(self.length):
            pw += random.choice(self.available_chars)
        return pw
    
    __next__ = next


#########
# Tests #
#########

def test_respects_passed_length():
    length_2 = SimplePasswordGenerator(length=2)
    length_2_it = iter(length_2)
    assert len(next(length_2_it)) == 2

    length_4 = SimplePasswordGenerator(length=4)
    length_4_it = iter(length_4)
    assert len(next(length_4_it)) == 4

    length_16 = SimplePasswordGenerator(length=16)
    length_16_it = iter(length_16)
    assert len(next(length_16_it)) == 16


def test_uses_available_chars():
    pass_gen = SimplePasswordGenerator(available_chars=['a', 'b'], length=2)
    it = iter(pass_gen)
    password = next(it)

    assert (
        set(password) == set(['a', 'b']) or
        set(password) == set(['a']) or
        set(password) == set(['b'])
    )
