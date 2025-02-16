import math


# a.
def power(a: int, b: int) -> int:
    return a ** b


# b.
def sqrt_po(a: float) -> float:
    return math.sqrt(a)


def sqrt_neg(a: float) -> float:
    if a < 0:
        raise ValueError("Sqrt is not defined for negative numbers")
    return math.sqrt(a)


# c.
def factorial_po(a: int) -> int:
    return math.factorial(a)


def factorial_neg(a: int) -> int:
    if a < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    return math.factorial(a)
