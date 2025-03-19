def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mult(x, y):
    return x * y


def div(x: float, y: float) -> float:
    try:
        return x / y
    except ZeroDivisionError:
        raise ValueError("cannot divide by zero")
