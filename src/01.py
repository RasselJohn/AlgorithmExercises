# Get prime numbers in interval.

def find_prime_numbers(left_border: int, right_border: int):
    """
    Return all prime numbers in interval.
    :param left_border: int
    :param right_border: int
    :return: generator

    >>> list(find_prime_numbers(2, 11))
    [2, 3, 5, 7, 11]
    >>> list(find_prime_numbers(22, 55))
    [23, 29, 31, 37, 41, 43, 47, 53]
    >>> list(find_prime_numbers(-2, 22))
    Traceback (most recent call last):
        ...
    ValueError: Incorrect borders.
    >>> list(find_prime_numbers(22, 1))
    Traceback (most recent call last):
        ...
    ValueError: Incorrect borders.
    """
    if left_border < 2 or left_border >= right_border:
        raise ValueError('Incorrect borders.')

    for i in range(left_border, right_border + 1):
        for j in range(2, i - 1):
            if i % j == 0:
                break
        else:
            yield i


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
