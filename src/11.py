# Script must:
# •	read text data;
# •	print 'n' max numbers from it.
# Extra conditions:
# •	number is any digits sequence;
# •	number can include max 1000 digits;
# •	script should get only 1 param - 'n';
# •	it must have tests;
# •	script has to be an execute file;
# •	text data(file) may be very big(40Gb!).


import heapq
import random
import string
import time
from traceback import format_exc


def generate_file_with_numbers(file_name, max_digit_counts=1001, exponent=100):
    file = open(file_name, 'w')

    for i in range(10 ** exponent):
        s = ''.join(
            random.choice(string.digits) for j in range(random.randint(1, max_digit_counts))
        )
        file.write('{}\n'.format(s))
        file.flush()

    file.close()


class NMaxHeap:
    def __init__(self, file_name, max_length=1000):
        self.final_collection = {}
        self.collection_keys = []
        self.length = 0
        self.max_length = max_length
        self.file_name = file_name

    def get_n_max(self, n_max_count=5):
        '''
        Return "n" max values.
        >>> little_obj.get_n_max(11)
        [990044880209748209880044990001, 980179043351949424651514881024, 970401776948916827855048229049, 960712373502810196866499608576, 951110130465771892558603515625, 941594350210212243162003506176, 932164339999243723852791405249, 922819411957263335393616461824, 913558883040682586951726894401, 904382075008804490010000000000, 895288314394846972076105514601]
        >>> little_obj.get_n_max(1)
        [990044880209748209880044990001]
        >>> little_obj.get_n_max(0)
        Traceback (most recent call last):
        ...
        ValueError: Param "n_max_count" must not be less 1.

        :param n_max_count: how many items need to get
        :return: "n" max values
        '''
        if n_max_count < 1:
            raise ValueError('Param "n_max_count" must not be less 1.')
        f = open(self.file_name, 'r')
        for line in f:
            number = int(line)
            l_num = len(line.strip())
            if l_num in self.final_collection:
                self.update_item(number, l_num)
            else:
                self.create_item(number, l_num)

        f.close()
        return heapq.nlargest(n_max_count, heapq.merge(*self.final_collection.values()))

    def create_item(self, number, l_num):
        if self.length < self.max_length:
            heapq.heappush(self.collection_keys, l_num)
            self.final_collection[l_num] = [number]
            self.length += 1
        else:
            if self.final_collection[self.collection_keys[0]][0] < number:
                heapq.heappop(self.final_collection[self.collection_keys[0]])

                if not self.final_collection[self.collection_keys[0]]:
                    heapq.heappop(self.collection_keys)

                heapq.heappush(self.collection_keys, l_num)
                self.final_collection[l_num] = [number]

    def update_item(self, number, l_num):
        if self.length < self.max_length:
            heapq.heappush(self.final_collection[l_num], number)
            self.length += 1
        else:
            if self.final_collection[self.collection_keys[0]][0] < number:
                heapq.heappush(self.final_collection[l_num], number)
                heapq.heappop(self.final_collection[self.collection_keys[0]])

                if not self.final_collection[self.collection_keys[0]]:
                    heapq.heappop(self.collection_keys)


if __name__ == '__main__':
    try:
        variant = input(
            'Insert "1" for generate file.\n'
            'Insert "2" for getting of n-max numbers from file.\n'
            'Insert "3" for running of tests.\n'
            'For exit insert "q".\nCommand:'
        )

        file_name = 'big_file'
        if variant == '1':
            sub_variant = input(
                f'Warning! There will be created file with name "{file_name}".\n'
                f'If this file exists - it will be overwritten.\n'
                f'For continue press "Enter".\n'
                f'For exit insert any symbol.\nCommand:'
            )
            if sub_variant:
                exit()

            # generate_file_with_numbers(file_name)
            print(f'File "{file_name}" with numbers was generated.')
        elif variant == '2':
            command = input(
                f'File with default name "{file_name}" will be read.\n'
                f'Warning! File must be in current directory with script!\n'
                f'For continue press "Enter".\n'
                f'For exit insert any symbol.\nCommand:'
            )
            if command:
                exit()

            n = int(input(f'Print "n"(integer =< 10 000).\nFor exit print "q".\nCommand:'))
            if n == 'q':
                exit()

            print("Process is becoming. Please, wait ...")
            start = time.time()
            n_max = NMaxHeap(file_name).get_n_max(n)
            for i in n_max:
                print(f'Result: {i}.\n')
            end = time.time()
            print('During: {} sec.'.format(end - start))
        elif variant == '3':
            import doctest

            doctest.testmod(verbose=True,
                            extraglobs={'little_obj': NMaxHeap('../assets/test_file')})
    except Exception:
        print(f'Error: {format_exc()}')
        exit()
