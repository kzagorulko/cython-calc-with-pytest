import pytest

from calc import Calc

calc = Calc()


def test_sum_small():
    a = 0.0000001
    b = 0.00000007

    assert calc.sum(a, b) == a + b


def test_sum_big():
    a = 700987100000
    b = 15700987100666

    assert calc.sum(a, b) == a + b


def test_div_zero():
    with pytest.raises(ZeroDivisionError):
        calc.divide(1, 0)


def test_zero_multiplication():
    a = 15
    b = 0

    assert calc.multiply(a, b) == 0


def test_f_lz():
    with pytest.raises(ValueError) as ex:
        calc.factorial(-5)

    assert str(ex.value) == 'Invalid argument, value less then 0'


def test_factorial_more_than_20():
    assert calc.factorial(21) == 51090942171709440000
