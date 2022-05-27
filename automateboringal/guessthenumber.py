import random

print("Hello. What is your name?")
name = input()

print('Hello, ' + name + '. I am thinking a number between 1 to 100 right now. Guess the number')
secret = random.randint(1, 100)

for guesses in range(1, 7):
    print("Take a guess: ")
    guess = int(input())

    if guess > secret:
        print("Your guess is higher than the answer")
    elif guess < secret:
        print("Your guess is lower than the answer")
    else:
        break;

if guess == secret:
    print('PERFECT JOB! ' + name + '! You have guessed the number correctly')
else:
    print('Bzzzzt. Your guesses are up. The number I was thinking of is ' + str(secret))