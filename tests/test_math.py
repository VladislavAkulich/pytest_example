from pytest import raises, mark


def test_one_plus_one():
    assert 1 + 1 == 2


# Test failure
# @mark.skip
def test_one_plus_two():
    a = 1
    b = 2
    c = 0
    assert a + b == c


# Exception handling
def test_divide_by_zero():
    with raises(ZeroDivisionError) as e:
        num = 1 / 0

    assert 'division by zero' in str(e.value)


products = [
    (2, 3, 6),
    (1, 99, 99),
    (0, 99, 0),
    (3, -4, -12),
    (-5, -5, 25),
    (2.5, 6.7, 16.75),
]


# Parametrized tests
@mark.parametrize('a, b, product', products)
def test_multiplication(a, b, product):
    assert a * b == product
