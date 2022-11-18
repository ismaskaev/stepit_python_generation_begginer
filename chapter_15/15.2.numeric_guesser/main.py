import random

def is_valid(string):
    result = True

    if string.isnumeric():
        result = 1 <= int(string) <= 100
    else:
        result = False
    return result

random_number = random.randint(1, 100)
print('Welcome to Number Guessing!')
try_count = 0

while True:
    print('Enter a number from 1 to 100:')
    text = input()
    if is_valid(text):
        number = int(text)
        try_count += 1
        if number == random_number:
            print(f'You guessed it, congratulations! Number of attempts: {try_count}' )
            print('Start a new game? (Y or N)')
            if input().lower() == 'y':
                random_number = random.randint(1, 100)
                continue
            else:
                break
            break
        elif number < random_number:
            print('Your number is less than what you have guessed, please try again.', end=' ')
        else:
            print('Your number is higher than expected, please try again.', end=' ')       
    else:
        print('Maybe we can still introduce an integer from 1 to 100?')
        continue

print('Thanks for playing the number guessing game. See you...')