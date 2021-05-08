# Script must check string with brackets on correctness.
# There are 3 different ways(functions) for checking.
# If string is correct - function returns 'Success'
# else position with symbol which breaks sequence.

from typing import Union


def quick_check(s: str) -> Union[int, str]:
    open_brackets = '([{'
    close_brackets = ')]}'
    ocb = {')': '(', ']': '[', '}': '{'}
    col = []

    for index, ch in enumerate(s, 1):
        if ch in open_brackets:
            col.append((index, ch))

        elif ch in close_brackets:
            if not col or col[-1][1] != ocb[ch]:
                return index

            col.pop()

    if col:
        return col[-1][0]

    return 'Success'


def middle_check(s: str) -> Union[int, str]:
    open_brackets = '([{'
    close_brackets = ')]}'
    ocb = {')': '(', ']': '[', '}': '{'}
    col = []

    for index, ch in enumerate(s):
        if ch in open_brackets:
            col.append(ch)
        elif ch in close_brackets:
            correspond_elem = ocb[ch]
            for j in range(index - 1, -1, -1):
                if col[j] is None:
                    continue

                if col[j] != correspond_elem:
                    return index + 1
                else:
                    col[j] = None
                    col.insert(index, None)
                    break
            else:
                return index + 1
        else:
            col.append(None)

    for i, el in enumerate(reversed(col)):
        if el is not None:
            return len(col) - i

    return 'Success'


def slow_check(s: str) -> Union[int, str]:
    open_brackets = ('(', '[', '{')
    close_brackets = (')', ']', '}')
    ocb = {')': '(', ']': '[', '}': '{'}
    c = {
        index: item
        for index, item in enumerate(s, 1) if item in open_brackets or item in close_brackets
    }

    cl: int = len(s) + 1
    for i in range(1, cl):
        item = c.get(i)
        if item in close_brackets:
            j: int = i - 1
            correspond_elem = ocb[item]
            while j != 0:
                if j in c:
                    if c[j] != correspond_elem:
                        return i
                    else:
                        del c[i]
                        del c[j]
                        break
                j -= 1
            else:
                return i

    if c:
        return max(c, key=lambda k: k)
    else:
        return 'Success'


if __name__ == '__main__':
    for func in (quick_check, middle_check, slow_check):
        print(f'Checking function: {func.__name__}')
        print('Checking...')

        assert func("([](){([])})") == 'Success'
        assert func("()[]}") == 5
        assert func("{{[()]]") == 7
        assert func("{{{[][][]") == 3
        assert func("{{") == 2
        assert func("{}") == 'Success'
        assert func("") == 'Success'
        assert func("}") == 1
        assert func("[]([]") == 3

        assert func("{{{**[][][]") == 3
        assert func("*{}") == 'Success'
        assert func("[]([];") == 3
        assert func("{*{{}") == 3
        assert func("[[*") == 2
        assert func("{*}") == 'Success'
        assert func("{{{**[][][]") == 3

        print('This completed!')
