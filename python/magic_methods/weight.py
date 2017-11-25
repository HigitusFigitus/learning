class Weight(object):
    def __init__(self, kilograms=None, pounds=None):
        if not any([kilograms, pounds]):
            raise ValueError('Unit of measure missing or invalid')

        self._kilograms = kilograms
        self._pounds = pounds

    @property
    def kilograms(self):
        return self._kilograms or self._pounds / 2.2

    @property
    def pounds(self):
        return self._pounds or self._kilograms * 2.2

    def __add__(self, other):
        if self._kilograms:
            return Weight(kilograms=(self.kilograms + other.kilograms))
        return Weight(pounds=(self.pounds + other.pounds))


#########
# Tests #
#########

import pytest

def test_add_only_pounds():
    w1 = Weight(pounds=37)
    w2 = Weight(pounds=22)
    w3 = w1 + w2
    assert w3.pounds == 59

def test_add_kilograms_to_pounds():
    w1 = Weight(kilograms=80)
    w2 = Weight(pounds=46)
    w3 = w1 + w2
    assert w3.kilograms == pytest.approx(100.90, rel=0.01)
    assert w3.pounds == pytest.approx(222.0, rel=0.01)

def test_add_only_kilograms():
    w1 = Weight(kilograms=80)
    w2 = Weight(kilograms=25)
    w3 = w1 + w2
    assert w3.kilograms == 105
