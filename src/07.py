def parse_haffman_code(coded_str: str, sym_table: dict):
    """
    Return string by Haffman's code.
    :param string: str
    :return: str
    >>> parse_haffman_code('0',{'0':'a'})
    'a'
    >>> parse_haffman_code('000',{'0':'b'})
    'bbb'
    >>> parse_haffman_code('01001100100111',{'0': 'a','10':'b','110':'c','111':'d'})
    'abacabad'
    """
    result = ''
    sub_str, coded_str = coded_str[0], coded_str[1:]
    while len(coded_str) != 0:
        if sub_str in sym_table:
            result += sym_table[sub_str]
            sub_str = coded_str[0]
        else:
            sub_str += coded_str[0]

        coded_str = coded_str[1:]

    if sub_str:
        result += sym_table[sub_str]

    return result


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
