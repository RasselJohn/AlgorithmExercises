# There are a integer number 'n'(1 ≤ n ≤ 10^5),
# and array A[1…n] from 'n' different natural numbers(1 ≤ A[i] ≤ 10^9) to increasing in first row.
# In second row there are a integer number 'k'(1 ≤ k ≤ 10^5) and
# and array B[1…k] from 'k' different natural numbers(1 ≤ B[j] ≤ 10^9).
# For each item in B should print index 'i'(1 ≤ i ≤n) for A[i]=B[j]
# else print '-1' if this item does not exist.


def get_item(arr, val):
    left_bound = 0
    arr_len = len(arr) - 1

    while left_bound <= arr_len:
        center = (left_bound + arr_len) // 2
        center_val = arr[center]

        if center_val == val:
            return center + 1
        elif center_val > val:
            arr_len = center - 1
        elif center_val < val:
            left_bound = center + 1

    return -1


def main(array_str, values_str):
    """
    >>> main('5 1 5 8 12 13', '5 8 1 23 1 11')
    3 1 -1 1 -1
    >>> main('1 1', '2 2 3')
    -1 -1
    >>> main('0', '2 2 3')
    -1 -1
    """

    # array_len, *array = [int(i) for i in input().split(' ')]
    # values_len, *values = [int(i) for i in input().split(' ')]
    array_len, *array = [int(i) for i in array_str.split(' ')]
    values_len, *values = [int(i) for i in values_str.split(' ')]
    print(' '.join(str(get_item(array, val)) for val in values))


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
