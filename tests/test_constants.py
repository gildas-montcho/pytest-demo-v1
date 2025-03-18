import pytest

from src import MIN_AGE, MAX_AGE


class TestConstants:
    def test_min_age_constant(self):
        assert MIN_AGE == 18

    def test_max_age_constant(self):
        assert MAX_AGE == 75
