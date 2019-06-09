# There are 'n'(1 ≤ n ≤ 10^4) natural numbers ≤ 10.
# Algorithm must print increasing sequence.


def print_increasing_sequence(numbers):
    """
    >>> print_increasing_sequence([3, 2, 4, 1, 10, 7, 5, 6, 9, 8])
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> print_increasing_sequence([2, 3, 9, 2, 9])
    [2, 2, 3, 9, 9]
    >>> print_increasing_sequence([])
    []
    """

    nums_len = len(numbers)
    res = [None] * nums_len
    b = [0] * 11

    for i in range(nums_len):
        b[numbers[i]] += 1

    for i in range(1, 11):
        b[i] += b[i - 1]

    for i in range(nums_len - 1, -1, -1):
        res[b[numbers[i]] - 1] = numbers[i]
        b[numbers[i]] -= 1

    return res


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
