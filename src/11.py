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


def generate_file_with_numbers(max_digit_counts=1001, file_name='test'):
    with open(file_name, 'w') as f:
        for i in range(10 ** 100):
            s = ''.join(
                random.choice(string.digits) for j in range(random.randint(1, max_digit_counts))
            )
            f.write('{}\n'.format(s))
            f.flush()


# generate_file_with_numbers()


class Nmax:
    def __init__(self, file_name):
        self.final_collection = {}
        self.collection_keys = []
        self.length = 0
        self.max_length = 100
        self.file_name = file_name

    def get_nmax(self, n_max_count=5):
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


start = time.time()

n_max = Nmax('test').get_nmax(100)
for i in n_max:
    print(f'Result: {i}\n.')

end = time.time()
print('Time: {}.'.format(end - start))
