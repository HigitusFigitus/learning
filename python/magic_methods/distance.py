class Distance(object):
    def __init__(self, meters=None, feet=None):
        # Please don't change this method
        if not any((meters, feet)):
            raise ValueError("Provide at least one measure of distance")

        self.meters = meters
        self.feet = feet

    @property
    def distance_in_meters(self):
        return self.meters or self.feet / 3.28
    
    @property
    def distance_in_feet(self):
        return self.feet or self.meters * 3.28
    
    @property
    def distance_in_miles(self):
        if self.feet:
            return self.feet * 0.00018939
        else:
            return round(self.meters * 0.00062137)
    
    @property
    def distance_in_kilometers(self):
        if self.feet:
            return self.feet / 3280.8
        else:
            return self.meters / 1000


#########
# Tests #
#########

import pytest

def test_meters_to_feet():
    d = Distance(meters=8000)
    assert d.distance_in_meters == 8000
    assert d.distance_in_feet == 26240

def test_meters_to_miles():
    d = Distance(meters=8000)
    assert d.distance_in_meters == 8000
    assert d.distance_in_miles == 5

def test_feet_to_kilometers():
    d = Distance(feet=25000)
    assert d.distance_in_feet == 25000
    assert d.distance_in_kilometers == pytest.approx(7.62, rel=1e-2)

def test_feet_to_meter():
    d = Distance(feet=25000)
    assert d.distance_in_feet == 25000
    assert d.distance_in_meters == pytest.approx(7621.95, rel=1e-2)

def test_meters_to_kilometers():
    d = Distance(meters=8000)
    assert d.distance_in_meters == 8000
    assert d.distance_in_kilometers == 8

def test_feet_to_miles():
    d = Distance(feet=25000)
    assert d.distance_in_feet == 25000
    assert d.distance_in_miles == pytest.approx(4.76, rel=1e-2)
