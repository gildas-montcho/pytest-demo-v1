from src.math_func import add, sub, mult, div
from pytest import approx


class TestFunctions:

    def test_add(self):
        assert add(5, 4) == 9

    def test_sub(self):
        assert sub(5, 4) == 1

    def test_mult(self):
        assert mult(5, 4) == 20

    def test_div(self):
        assert div(5, 4) == approx(1.25)
