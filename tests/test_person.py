from src.person.person import Person
import pytest


class TestPerson:
    @pytest.mark.parametrize(
        "name,age,is_retired", [("Soren", 20, False), ("Martine", 75, True)]
    )
    def test_name_and_age(self, name, age, is_retired):
        p = Person(name, age)
        assert p.name == name
        assert p.age == age
        assert p.is_retired == is_retired

    def test_no_name_raises_exception(self):
        with pytest.raises(ValueError):
            Person("", 20)

    def test_age_less_than_18_raises_exception(self):
        with pytest.raises(ValueError):
            Person("Bob", 17)

    def test_age_less_more_75_raises_exception(self):
        with pytest.raises(ValueError):
            Person("Bob", 76)

    @pytest.mark.parametrize("name", ["Bob", "bob", "BOB"])
    def test_capitalize_name(self, name):
        p = Person(name, 20)
        assert p.name == "Bob"

    def test_strip_name(self):
        p = Person("  bob  ", 20)
        assert p.name == "Bob"

    def test_str(self):
        name, age = "Albert", 24
        p = Person(name, age)
        assert str(p) == f"{name.capitalize()} is {age} years old"

    def test_repr(self):
        name, age = "Albert", 24
        p = Person(name, age)
        assert repr(p) == f"Person(name='{name}', age={age})"
