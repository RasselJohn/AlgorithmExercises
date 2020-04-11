# Convert greek number to arabic number.
from functools import reduce


def convert_greek_number_to_arabic(greek_num):
    """
    Convert greek number to arabic number
    :param greek_num: str
    :return: int
    >>> convert_greek_number_to_arabic('I')
    1
    >>> convert_greek_number_to_arabic('IV')
    4
    >>> convert_greek_number_to_arabic('VI')
    6
    >>> convert_greek_number_to_arabic('IX')
    9
    >>> convert_greek_number_to_arabic('X')
    10
    >>> convert_greek_number_to_arabic('XI')
    11
    >>> convert_greek_number_to_arabic('XLII')
    42
    >>> convert_greek_number_to_arabic('XCIV')
    94
    >>> convert_greek_number_to_arabic('CDXCIX')
    499
    >>> convert_greek_number_to_arabic('MCMXCI')
    1991
    >>> convert_greek_number_to_arabic('')
    Traceback (most recent call last):
        ...
    ValueError: Incorrect greek number.
    >>> convert_greek_number_to_arabic('FF')
    Traceback (most recent call last):
        ...
    ValueError: Incorrect greek number.
    """
    link = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    if not greek_num or any(g not in link.keys() for g in greek_num):
        raise ValueError('Incorrect greek number.')

    num_list = [link[greek_num[0]]]
    for ch in greek_num[1:]:
        n = link[ch]
        if n > num_list[-1]:
            num_list[-1] = n - num_list[-1]
        else:
            num_list.append(n)

    return reduce((lambda x, y: x + y), num_list)


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
