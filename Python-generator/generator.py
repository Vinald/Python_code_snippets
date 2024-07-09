'''
Generators are iterators, a kind of iterable you can only iterate over once. 
Generators do not store all the values in memory, they generate the values on the fly.
'''

# normal function
def square_numbers(nums):
    result = []
    for num in nums:
        result.append(num * num)
    return result


# converting it to a generator
def square_numbers_gen(nums):
    for num in nums:
        yield num * num


# set of numbers
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# callng the normal function
num1 = square_numbers(nums)
print('Normal function: ', num1)
print()


# Comprehesion function
num1 = [num * num for num in nums]
print('Comprehesion Normal function: ', num1)
print()


# converting a compression function to a generator function
num1 = (num * num for num in nums)
print('Generator function: ', next(num1))
print('Generator function: ', next(num1))
print('Generator function: ', next(num1))
print('Generator function: ', next(num1))
print()

# calling generator function
num1 = square_numbers_gen(nums)
# print('Generator function: ', next(num1))
# print('Generator function: ', next(num1))
# print('Generator function: ', next(num1))
# print('Generator function: ', next(num1))
# print('Generator function: ', next(num1))
# print('Generator function: ', next(num1))
# print('Generator function: ', next(num1))
# print('Generator function: ', next(num1))
# print('Generator function: ', next(num1))
for num in num1:
    print('Generator function: ', num)
print()
