def is_prime(number):
    """
    If number is prime - return True
    :param number: int
    :return: boolean

    >>> is_prime(25)
    False
    >>> is_prime(12)
    False
    >>> is_prime(11)
    True
    >>> is_prime(1)
    Traceback (most recent call last):
        ...
    ValueError: Number must be more than 2!
    >>> is_prime(-12)
    Traceback (most recent call last):
        ...
    ValueError: Number must be more than 2!
    """
    import math

    if number < 2:
        raise ValueError("Number must be more than 2!")

    if number // 2 == 0:
        return False

    k = 3
    t = math.floor(number ** 0.5)
    while (k <= t) and ((number % k) != 0):
        k += 2

    return k > t


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
