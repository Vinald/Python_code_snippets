import time
'''
decorators are a way to modify or extend the behavior of functions or methods without changing their code
'''


# first way of using decorators
def start_end_decorator(function):
    def wrapper(*args, **kwargs):
        print("before decorator")
        function()
        print("after decorator")
    return wrapper


def say_hello():
    print("Hello")


print()
say_hello()
print()


print()
start_end_decorator(say_hello)()
print()


# Second way of using decorators
@start_end_decorator
def name():
    print("Samuel")


print()
name()
print()


# Third way with return
def my_decorator(function):
    def wrapper(*args, **kwargs):
        print("before decorator")
        ret = function(*args, **kwargs)
        # print("after decorator")
        return ret
    return wrapper


@my_decorator
def names(name):
    return f'name {name}'


print()
name = names('vinald')
print(name)
print()


# Timing decorator
def timing(function):
    def wrapper(*args, **kwargs):
        start = time.time()
        ret = function(*args, **kwargs)
        end = time.time()
        print(f'{function.__name__} took {end - start} seconds')
        return ret
    return wrapper  


# practical use 
# logging
def logged(function):
    def wrapper(*args, **kwargs):
        value = function(*args, **kwargs)
        with open('login.txt', 'a+') as f:
            fname = function.__name__
            print(f'{fname} {value}')
            f.write(f'{fname}: {value}\n')
        return value
    
    return wrapper


def adding(x, y):
    return x + y


add1 = adding(1, 3)
print()
print(add1)
print()


@timing
@logged
def multi(x, y):
    return x * y


mul1 = multi(2, 3)
print(mul1)
print()


# counter
class CounterCall:
    def __init__(self, function):
        self.count = 0
        self.function = function

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f'function {self.function.__name__} was called {self.count} time(s)')
        return self.function(*args, **kwargs)
    

@CounterCall
def adding(x, y):
    return x + y


print()
add1 = adding(2, 1)
print(add1)

add1 = adding(2, 2)
print(add1)

add1 = adding(2, 5)
print(add1)
