from src.person.person import Person
import pytest


class TestPerson:
    def test_name_and_age(self):
        p = Person("Bob", 20)
        assert p.name == "Bob"
        assert p.age == 20

    def test_no_name_raises_exception(self):
        with pytest.raises(ValueError):
            Person("", 20)

    def test_age_less_than_18_raises_exception(self):
        with pytest.raises(ValueError):
            Person("Bob", 17)

    def test_age_less_more_75_raises_exception(self):
        with pytest.raises(ValueError):
            Person("Bob", 76)
