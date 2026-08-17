from calculator import multiplication
import pytest

def test_addition():
    assert multiplication('10*3') == 30
    assert multiplication('3* -12 ') == -36
    assert multiplication('    14 * 1 ') == 14
    assert multiplication('    14 * 0 ') == 0
    with pytest.raises(ValueError):
        multiplication('5 multiplied by 5')
