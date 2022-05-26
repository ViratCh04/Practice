import random
import time

def intro():
    print("left or right?")
    print()

def choosedirecn():
    cave = ''
    while cave != '1' and cave != '2':
        print("Which cave will you pick?(1 or 2)")
        cave = input()

    return cave

def excursion(choice):
    print("It is dark.....")
    time.sleep(2)
    print("You hear some noise....")
    time.sleep(2)
    print("A large dragon jumps at you and.........")
    print()
    time.sleep(2)

    eventdragon = random.randint(1,2)

    if choice == str(eventdragon):
        print("gives you his treasure!")
    else:
        print("gobbles you down!")

answer = "yes"
while answer == "yes" or answer == "y":
    intro()
    choice = choosedirecn()
    excursion(choice)

    print("Want to play again ? (y/n)")
    answer = input()