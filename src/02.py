def get_sequence_by_result_sum(numbers: list, result_sum: int):
    """
    Return all sequence with numbers and operators '+' or '-',
    where result equals result_sum.
    If it cannot - return None
    :param numbers: list of int
    :param result_sum: int
    :return: sequence

    >>> list(get_sequence_by_result_sum([5, 3, 2, 1, 5, 3, 8],7))
    ['5 + 3 - 2 + 1 + 5 + 3 - 8 = 7', '5 + 3 - 2 + 1 - 5 - 3 + 8 = 7', '5 - 3 - 2 + 1 - 5 + 3 + 8 = 7']

    >>> list(get_sequence_by_result_sum([2,2],4))
    ['2 + 2 = 4']

    >>> list(get_sequence_by_result_sum([2,3],4))
    []

    >>> list(get_sequence_by_result_sum([],10))
    Traceback (most recent call last):
        ...
    ValueError: Incorrect numbers list.

    >>> list(get_sequence_by_result_sum([1],1))
    Traceback (most recent call last):
        ...
    ValueError: Incorrect numbers list.
    """

    if not numbers or len(numbers) < 2:
        raise ValueError('Incorrect numbers list.')

    operations = ['-' for i in range(1, len(numbers))]
    oper_len = len(operations)
    curr_sum = 0
    repeat_count = 2 ** (len(numbers) - 1)

    while repeat_count > 0:

        for i in range(0, oper_len):
            if operations[i] == '-':
                operations[i] = '+'
                break
            else:
                operations[i] = '-'

        curr_sum = numbers[0]
        for i in range(0, oper_len):
            if operations[i] == '+':
                curr_sum += numbers[i + 1]
            else:
                curr_sum -= numbers[i + 1]

        # return all variants
        if result_sum == curr_sum:
            second_part = ' '.join(f'{operations[i]} {numbers[i + 1]}' for i in range(0, oper_len))
            yield f'{numbers[0]} {second_part} = {result_sum}'

        repeat_count -= 1


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
