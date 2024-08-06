from functools import reduce
'''
reduce() function is used to apply a particular function passed in its argument to all of the list elements mentioned in the sequence passed along. This function is defined in “functools” module.
'''
# Example 1
e = [1, 2, 3, 4, 5]
sum = reduce(lambda x, y: x + y, e)
print(sum)
print()

# Example 2
f = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, f)
print(product)
print()

# Example 3
g = [1, 2, 3, 4, 5]
max = reduce(lambda x, y: x if x > y else y, g)
print(max)
print()