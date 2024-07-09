name = 'samuel'

print('Hello, %s' % name)
print('Hello, {}'.format(name))
print(f'Hello, {name}')

# padding
print('Hello, %10s' % name)
print('Hello, {:>10}'.format(name))
print(f'Hello, {name:<10}')
print(f'Hello, {name:^10}')

# numbers
num = 1000000
print('The number is %d' % num)
print('The number is {:d}'.format(num))
print(f'The number is {num}')
print(f'The number is {num:d}')
print(f'The number is {num:E}')
print(f'The number is {num:X}')
print(f'The number is {num:,}')
