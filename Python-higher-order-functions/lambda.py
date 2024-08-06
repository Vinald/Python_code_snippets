'''
lambda function
name = lambda function arguments, expression: return expression
'''
# lambda function
adding = lambda x: x+10
print(adding(20))
print()

sum1 = lambda a, b: a + b
print(f'lambda function {sum1(2, 2)}')
print()

double = lambda x: x * 2
print(double(5))
print()

sum1 = lambda *numbers: sum(numbers)
print(sum1(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)) 
print()

full_name = lambda first_name, last_name: f'{first_name} {last_name}'
print(full_name('John', 'Doe'))
print()
