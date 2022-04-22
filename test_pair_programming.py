import pytest
from main_pair_programming import Integer


def test_max():
    a = Integer(-2)
    b = Integer(5)
    assert max(a, b) == 5

    
def test_min():
    a = Integer(-2)
    b = Integer(5)
    assert min(a, b) == -2
