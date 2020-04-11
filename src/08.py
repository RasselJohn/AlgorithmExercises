# Realizing of max-heap.

class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)

        len_heap = len(self.heap)
        if len_heap <= 3:
            self.heap.sort(reverse=True)
            return

        curr = len_heap - 1
        new_curr = (curr - 1) // 2

        while 0 <= new_curr and self.heap[curr] > self.heap[new_curr]:
            self.reverse(curr, new_curr)
            curr = new_curr
            new_curr = (curr - 1) // 2

    def get_max(self):
        mx = self.heap[0]
        if len(self.heap) == 1:
            self.heap = []
            return mx

        self.heap[0] = self.heap.pop()
        len_heap = len(self.heap)
        if len_heap <= 3:
            self.heap.sort(reverse=True)
            return mx

        curr = 0
        if self.heap[curr] >= self.heap[1] and self.heap[curr] >= self.heap[2]:
            return mx

        next_index = 1
        while 0 <= next_index < len_heap:

            if next_index + 1 < len_heap:
                if (self.heap[next_index] > self.heap[curr]
                        and self.heap[next_index] >= self.heap[next_index + 1]):
                    self.reverse(curr, next_index)
                    curr, next_index = next_index, next_index * 2 + 1

                elif (self.heap[next_index + 1] > self.heap[curr]
                      and self.heap[next_index + 1] > self.heap[next_index]):
                    self.reverse(curr, next_index + 1)
                    curr, next_index = next_index + 1, (next_index + 1) * 2 + 1
                else:
                    break
            elif self.heap[next_index] > self.heap[curr]:
                self.reverse(curr, next_index)
                break
            else:
                break

        return mx

    def reverse(self, first, second):
        self.heap[first], self.heap[second] = self.heap[second], self.heap[first]


def max_heap_handler(commands):
    """
    Return max values by commands.
    :param commands: str
    :return: None
    >>> max_heap_handler(r'''Insert 2
    ... Insert 3
    ... Insert 18
    ... Insert 15
    ... Insert 18
    ... Insert 12
    ... Insert 12
    ... Insert 2
    ... ExtractMax
    ... ExtractMax
    ... ExtractMax
    ... ExtractMax
    ... ExtractMax
    ... ExtractMax
    ... ExtractMax''')
    18
    18
    15
    12
    12
    3
    2
    >>> max_heap_handler(r'''Insert 200
    ... Insert 10
    ... ExtractMax
    ... Insert 5
    ... Insert 500
    ... ExtractMax''')
    200
    500
    >>> max_heap_handler(r'''Insert 200
    ... Insert 10
    ... Insert 5
    ... Insert 500
    ... ExtractMax
    ... ExtractMax
    ... ExtractMax
    ... ExtractMax''')
    500
    200
    10
    5
    >>> max_heap_handler(r'''Insert 323123123
    ... Insert 100000000
    ... Insert 323123123
    ... Insert 100000000
    ... Insert 323123123
    ... Insert 100000000
    ... Insert 323123123
    ... Insert 100000000
    ... Insert 323123123
    ... Insert 100000000
    ... Insert 323123123
    ... Insert 100000000
    ... Insert 323123123
    ... Insert 100000000
    ... Insert 323123123
    ... Insert 100000000
    ... ExtractMax
    ... ExtractMax
    ... ExtractMax
    ... ExtractMax
    ... ExtractMax
    ... ExtractMax
    ... ExtractMax
    ... ExtractMax
    ... ExtractMax
    ... ExtractMax
    ... ExtractMax
    ... ExtractMax
    ... ExtractMax
    ... ExtractMax
    ... ExtractMax
    ... ExtractMax''')
    323123123
    323123123
    323123123
    323123123
    323123123
    323123123
    323123123
    323123123
    100000000
    100000000
    100000000
    100000000
    100000000
    100000000
    100000000
    100000000
    >>> max_heap_handler(r'''Insert 53
    ... Insert 7
    ... Insert 22
    ... Insert 6
    ... Insert 5
    ... Insert 21
    ... Insert 20
    ... ExtractMax
    ... ExtractMax
    ... ExtractMax
    ... ExtractMax
    ... ExtractMax
    ... ExtractMax
    ... ExtractMax''')
    53
    22
    21
    20
    7
    6
    5
    >>> max_heap_handler(r'''Insert 10
    ... Insert 10
    ... Insert 8
    ... ExtractMax
    ... ExtractMax
    ... ExtractMax''')
    10
    10
    8
    """

    h = MaxHeap()
    for c in commands.split('\n'):
        command = c.split(' ')

        if len(command) > 1:
            val = int(command[1])
            h.insert(val)
        else:
            print(h.get_max())


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
