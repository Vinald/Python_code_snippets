'''
map(function, iterable)
- The map() function applies a given function to each item of an iterable (list, tuple etc.) and returns a list of the results.
- The returned value from map() (map object) then can be passed to functions like list() (to create a list), set() (to create a set) and so on.
'''

# Example 1
store = [('shirt', 20.0), ('pants', 20.0), ('jacket', 36.0), ('cap', 12.0)]
to_euros = lambda data: (data[0], data[1]*0.82)


store_euros = map(to_euros, store)
print(list(store_euros))
print()


# Example 2
my_list = [1, 2, 3, 4, 5]
double_num = map(lambda num: num * 2, my_list)
print(list(double_num))
print()

