def hello(name):
    print("HOWDY, " + name)

hello("Baba")
hello("fart")

def plusone(num):
    return num + 1

nom = 12
nom = plusone(nom)
print(nom)

def spam():
    global eggs
    eggs = 'yaahooo'

eggs = 490
spam()
print(eggs)

print('hello, ', end='')
print('world (with end keyword argument)')

print('cat', 'dog', 'lion')
print('cat', 'dog', 'lion', sep=' 3.14 ')
for i in range(1, 5):
    print('...')

import random

def _8ball(number):
    if number == 1:
        return "Not really"
    elif number == 2:
        return "Dont even try"
    elif number == 3:
        return "Go ahead"
    elif number == 4:
        return "Absolutely"
    elif number == 5:
        return "Yes"
    elif number == 6:
        return "I doubt that"
    elif number == 7:
        return "You need help"
    elif number == 8:
        return "Try again"
    elif number == 9:
        return "......."
    
print("8ball time!")
print("Think of a yes/no question and the 8ball will guide your future")
input()
print(_8ball(random.randint(1, 10)))