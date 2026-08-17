from calculator import division
import pytest

def test_addition():
    assert division('5/2') == 2.5
    assert division('-12/ 1 ') == -12
    assert division('    12 / 1 ') == 12
    with pytest.raises(ValueError):
        division('5 plus 5')
    with pytest.raises(ZeroDivisionError):
        division('1/0')
