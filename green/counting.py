from blue.greeting import greet


def count(n):

    for i in range(n):
        print(f"{i:2d}: {greet()}")
