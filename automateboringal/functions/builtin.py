import random

print(random.randint(1, 10))
print(random.randint(1, 999))

import os, math
from sys import *       # imports all functions so you don't have to use the module name before it everytime

# Generally speaking, importing modules using the very first(or, second) method above is recommended as it helps to distinguish
# which function belongs to which module

print("HI!!")

import pyperclip

pyperclip.copy("VAHOOOO")
ayo = pyperclip.paste()
# the copy function also copies the string to your clipboard so it is useful for copying large amounts of text
print(ayo)
