from src.constants import MIN_AGE, MAX_AGE


class Person:
    def __init__(self, name: str, age: int):
        if not name:
            raise ValueError("name cannot be empty")
        if age < MIN_AGE or age > MAX_AGE:
            raise ValueError(f"age must be between {MIN_AGE} and {MAX_AGE}")

        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"
