from itertools import product, permutations, accumulate, combinations, groupby, cycle, count, repeat, combinations_with_replacement


'''
iterator is an object that contains a countable number of values
 methods iter() and next() are used to iterate through an iterable
__iter__() and __next__() are used to create an iterator
'''


# Custom iterator
class ListIterator:
    def __init__(self, list):
        self.__list = list
        self.__index = -1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.__index += 1
        if self.__index < len(self.__list):
            return self.__list[self.__index]
        else:
            raise StopIteration


my_list = [1, 2, 3, 4, 5]
my_iter = ListIterator(my_list)
print('Custom iterator')
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
# print(next(my_iter))
print()


# Iterator using iter() and next()
my_iter = iter(my_list)
print('Using iter() and next()')
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print()

# product
a = [1, 2]
b = [3, 4]
prod = product(a, b)
print(f'Product: {list(prod)}')
print()


# combinations
c = [1, 2, 3]
comb = combinations(c, 2)
print(f'Combination: {list(comb)}')
print()

# permutations
perm = permutations(c, 2)
print(f'Permutations: {list(perm)}')
print()

# groupby
d = [1, 2, 3, 4, 5, 6]


def smaller_than_4(x):
    return x < 4


group_obj = groupby(d, key=smaller_than_4)
for key, value in group_obj:
    print(key, list(value))
print()

# accumulate
e = [1, 2, 3, 4, 5, 3, 6, 7, 2]
acc = accumulate(e)
print(f'Original: {e}')
print(f'Accumulate: {list(acc)}')
print()


# count
for i in count(10):
    print(i)
    if i == 15:
        break
print()

# cycle
f = [1, 2, 3]
for i in cycle(f):
    print(i)
    if i == 3:
        break
print()

# repeat
g = [1, 2, 3]
for i in repeat(g, 3):
    print(i)
print()

#  combinations_with_replacement
h = [1, 2, 3]
comb = combinations_with_replacement(h, 2)
print(f'Combinations with replacement: {list(comb)}')
print()