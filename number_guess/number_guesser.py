import random

print('Welcome to the number guessing game\n')
top_number = input('Enter a maximum range to guess from: \n')

if top_number.isdigit():
    top_number = int(top_number)

    if top_number <= 0:
        print('Please enter a number greater than zero')
        quit()
else:
    print('Please enter a number next time\n')
    quit()


random_number = random.randint(0, top_number)
guesses = 0

while True:
    guesses += 1

    user_guess = input(f'Make a guess of a random number between 0 and {top_number}\n')
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please enter a number next time\n')
        continue

    if user_guess == random_number:
        print('Correct guess')
        break
    elif user_guess > random_number:
        print('Invalid guess, above the random number!\n')
    else:
        print('Invalid guess, below the random number!\n')


print(f'You got it in {guesses} guesses')