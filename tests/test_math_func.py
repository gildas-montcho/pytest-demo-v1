import pytest

from src.math_func import add, sub, mult, div
from pytest import approx


class TestMathFunc:

    @pytest.mark.parametrize(
        "num1, num2, expected", [(5, 4, 9), (15, 5, 20), (3, 7, 10)]
    )
    def test_add(self, num1, num2, expected):
        assert add(num1, num2) == expected

    def test_sub(self):
        assert sub(5, 4) == 1

    def test_mult(self):
        assert mult(5, 4) == 20

    def test_div(self):
        assert div(5, 4) == approx(1.25)

    def test_div_zero(self):
        with pytest.raises(ValueError) as exc_info:
            div(5, 0)

        assert str(exc_info.value) == "cannot divide by zero"
