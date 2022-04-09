# 2 int numbers 'n','m' are given.
# If anyone divides to another - print '1' otherwise '0'.
# Attention! Conditions and loops ('if', 'while') are banned!

def check_division(n: int, m: int) -> int:
    """
    >>> check_division(2, 8)
    1
    >>> check_division(2, 2)
    1
    >>> check_division(3, 4)
    0
    >>> check_division(12, 16)
    0
    >>> check_division(7, 14)
    1
    """

    return int(not bool((n % m) * (m % n)))


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
