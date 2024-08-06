'''
closure is a function that returns a function
'''


# Example 1
def outer_function():
    message = 'Hi'

    def inner_function():
        print(message)
    return inner_function


my_func = outer_function()
my_func()


# Example 2
def outer_function(message):
    def inner_function():
        print(message)
    return inner_function


hi_func = outer_function('Hi')
hello_func = outer_function('Hello')

hi_func()
hello_func()