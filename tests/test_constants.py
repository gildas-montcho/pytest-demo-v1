from src.constants import MIN_AGE, MAX_AGE, RETIRING_AGE


class TestConstants:
    def test_min_age_constant(self):
        assert MIN_AGE == 18

    def test_max_age_constant(self):
        assert MAX_AGE == 75

    def test_min_age_less_than_max_age(self):
        assert MIN_AGE < MAX_AGE

    def test_retiring_age_constant(self):
        assert RETIRING_AGE == 65

    def test_retiring_age_more_than_min_age(self):
        assert RETIRING_AGE > MIN_AGE

    def test_retiring_age_less_than_max_age(self):
        assert RETIRING_AGE < MAX_AGE
