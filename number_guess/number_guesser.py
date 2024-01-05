import random

print('Welcome to the number guessing game\n')
top_number = input('Enter a number: \n')

if top_number.isdigit():
    top_number = int(top_number)

    if top_number <= 0:
        print('Please enter a number greater than zero')
        quit()
else:
    print('Please enter a number next time\n')
    quit()

random_number = random.randint(0, top_number)


while True:
    



print(random_number)