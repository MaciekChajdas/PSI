import pytest
from main_pair_programming import Integer


def test_max():
    a = Integer(-2)
    b = Integer(5)
    assert max(a, b) == 5