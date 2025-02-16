import pytest
import calculator


# b.
def test_calculator_sqrt_9():
    # Arrange
    a = 9
    expected = 3.0

    # Act
    actual = calculator.sqrt_po(a)

    # Assert
    assert expected == actual, f"sqrt function failed for {a}"


# c + i.
def test_calculator_factorial_3_5_1():
    # Arrange
    a = 3
    expected = 6

    # Act
    actual = calculator.factorial_po(a)

    # Assert
    assert expected == actual, f"Expected {expected}, but got {actual}"

    # Arrange
    a = 5
    expected = 120

    # Act
    actual = calculator.factorial_po(a)

    # Assert
    assert expected == actual, f"Expected {expected}, but got {actual}"

    # Arrange
    a = 0
    expected = 1

    # Act
    actual = calculator.factorial_po(a)

    # Assert
    assert expected == actual, f"Expected {expected}, but got {actual}"

    # Arrange
    a = 1
    expected = 1

    # Act
    actual = calculator.factorial_po(a)

    # Assert
    assert expected == actual, f"Expected {expected}, but got {actual}"


def test_calculator_factorial_negative():
    with pytest.raises(ValueError):
        calculator.factorial_neg(-5)


# d.
def test_calculator_power_2_4():
    # Arrange
    a = 2
    b = 4
    expected = 16

    # Act
    actual = calculator.power(a, b)

    # Assert
    assert expected == actual, f"power function failed for {a} and {b}"


# e.
def test_calculator_power_3_2():
    # Arrange
    a = 3
    b = 2
    expected = 9

    # Act
    actual = calculator.power(a, b)

    # Assert
    assert expected == actual, f"power function failed for {a} and {b}"


# f.
def test_calculator_sqrt_25():
    # Arrange
    a = 25
    expected = 5.0

    # Act
    actual = calculator.sqrt_po(a)

    # Assert
    assert expected == actual, f"sqrt function failed for {a}"


# g.
def test_check_error_happened():
    # Arrange
    a = -5

    # Act and Assert
    with pytest.raises(ValueError) as ex:
        calculator.sqrt_neg(a)

    # Assert
    assert str(ex.value) == "Sqrt is not defined for negative numbers"


# h.
def test_calculator_factorial_4():
    # Arrange
    a = 4
    expected = 24

    # Act
    actual = calculator.factorial_po(a)

    # Assert
    assert expected == actual, f"Expected {expected}, but got {actual}"


# j.
def test_calculator_factorial_negative():
    # Arrange
    a = -3

    # Act
    with pytest.raises(ValueError) as ex:
        calculator.factorial_neg(a)

    # Assert
    assert str(ex.value) == "Factorial is not defined for negative numbers"
