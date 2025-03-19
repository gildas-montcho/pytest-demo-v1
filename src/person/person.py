from src.constants import MIN_AGE, MAX_AGE, RETIRING_AGE


class Person:
    def __init__(self, name: str, age: int):
        if not name:
            raise ValueError("name cannot be empty")
        if age < MIN_AGE or age > MAX_AGE:
            raise ValueError(f"age must be between {MIN_AGE} and {MAX_AGE}")

        self.name = name.strip().capitalize()
        self.age = age
        if self.age >= RETIRING_AGE:
            self.is_retired = True
        else:
            self.is_retired = False

    def __str__(self) -> str:
        return f"{self.name} is {self.age} years old"

    def __repr__(self) -> str:
        return f"Person(name='{self.name}', age={self.age!r})"
