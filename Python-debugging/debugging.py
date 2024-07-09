# import pdb; pdb.set_trace()

'''
Debugging using pdb
'''


def add(x, y):
    sum = x + y
    return sum


if __name__ == '__main__':
    x = int(input('Enter first number: '))
    y = int(input('Enter second number: '))
    sum = add(x, y)
    print(f'The sum of {x} and {y} is {sum}')
