# By the number 'n' (1≤n≤10^9) find max number 'k',
# which allows to set 'n' like a sum of 'k' different(!)  summands.
# Function must return array of summands(where len(summands)==k)

def get_summands(n):
    """
    >>> get_summands(1)
    [1]
    >>> get_summands(2)
    [2]
    >>> get_summands(7)
    [1, 2, 4]
    >>> get_summands(51)
    [1, 2, 3, 4, 5, 6, 7, 8, 15]
    >>> get_summands(777)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 74]
    """
    if n == 1 or n == 2:
        return [n]

    full_sum = 0
    summands = []

    for next_num in range(1, n):
        curr_sum = full_sum + next_num

        if curr_sum < n:
            summands.append(next_num)
            full_sum = curr_sum
        elif curr_sum == n:
            summands.append(next_num)
            break
        else:  # curr_sum > n
            summands.append(summands.pop() + 1)

            full_sum += 1
            if full_sum == n:
                break

    return summands


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
