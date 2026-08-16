from calculator import addition
import pytest

def test_addition():
    assert addition('5+2') == 7
    assert addition('-12+ 13 ') == 1
    assert addition('    12 + 1 ') == 13
    with pytest.raises(ValueError):
        addition('5 plus 5')
