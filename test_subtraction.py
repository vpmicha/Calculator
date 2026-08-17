from calculator import subtraction
import pytest

def test_addition():
    assert subtraction('10-3') == 7
    assert subtraction('3- 12 ') == -9
    assert subtraction('    14 - 1 ') == 13
    with pytest.raises(ValueError):
        subtraction('5 minus 5')
