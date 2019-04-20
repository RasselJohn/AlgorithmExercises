# Huffman coding
from collections import Counter

sorted_tree = lambda tree: sorted(tree, key=lambda ss: ss[0], reverse=True)


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree:
    def __init__(self):
        self.sym_table = {}

    def tree_passer(self, tree, appender=''):
        if tree.val:
            self.sym_table[tree.val] = appender

        if tree.left:
            self.tree_passer(tree.left, appender + '1')

        if tree.right:
            self.tree_passer(tree.right, appender + '0')


def haffman_code(string: str):
    """
    Return Haffman's code for string.
    :param string: str
    :return: str
    >>> haffman_code('a')
    '0'
    >>> haffman_code('abacabad')
    '01001100100111'
    >>> haffman_code('aaaa')
    '0000'
    >>> haffman_code('010010010010010010010010010010')
    '010010010010010010010010010010'
    >>> haffman_code('')
    Traceback (most recent call last):
        ...
    ValueError: String empty.
    """
    if len(string) < 1:
        raise ValueError('String empty.')

    counter = Counter(string)
    tree = sorted_tree([[frequency, Node(symbol)] for symbol, frequency in counter.items()])

    if len(tree) == 1:
        return ''.join('0' for i in string)

    while len(tree) > 1:
        t1, t2 = tree.pop(), tree.pop()
        tree.append([t1[0] + t2[0], Node(None, t1[1], t2[1])])
        tree = sorted_tree(tree)

    tr = Tree()
    tr.tree_passer(tree[0][1])
    coded_str = ''.join(tr.sym_table[i] for i in string)

    return coded_str


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
