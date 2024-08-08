'''
filter() is a built-in function in Python that is used to filter a sequence of elements for which a function returns a boolean (True, False).
'''

# Example 1
number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_num = filter(lambda  num: num % 2 == 0, number)

print(list(even_num))
print()

# Example 2
store = [('shirt', 20.0), ('pants', 20.0), ('jacket', 36.0), ('cap', 12.0)]
expensive = filter(lambda data: data[1] > 20, store)

print(list(expensive))
print()

oddNumber = filter(lambda num: num % 2 == 0, number)
print(list(oddNumber))