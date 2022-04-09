# Collection of commands are given
# (correct sequence of commands are guaranteed ).

# Function adds/removes int numbers in stack
# and control max value with access O(1).

# Type of commands:
# 'push <num>' - add to stack,
# 'pop' - remove from stack,
# 'max' - just print max.


import typing as T


def max_stack(commands: str) -> T.Generator[int, None, None]:
    """
    >>> list(max_stack(['push 2', 'push 1', 'max', 'pop', 'max']))
    [2, 2]
    >>> list(max_stack(['push 1', 'push 2', 'max', 'pop', 'max']))
    [2, 1]
    >>> list(max_stack(['push 4', 'max', 'push 5', 'max', 'pop', 'max']))
    [4, 5, 4]
    """
    stack = []
    max_stack = []

    for command in commands:
        if command == 'pop':
            stack.pop()
            max_stack.pop()

        elif command == 'max':
            yield max_stack[-1]

        else:  # for 'push <num>'
            num = int(command.split(' ')[1])
            stack.append(num)

            if max_stack:
                max_elem = max_stack[-1]
                max_stack.append(num if max_elem < num else max_elem)
            else:
                max_stack.append(num)


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
