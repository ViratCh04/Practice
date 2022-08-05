# Strings are immutable(cannot be modified)

a = 'This is Bob\'s cat'
print(a)

b = '\"man \n can \n ban\t \\ \tfan \"'
print(b)

print(r'As I\'m a good\n boy')
print()
print("""This is an 
extortion, and one
which would cost you 
dearly""")
print()

saa = """This is not an 
extortion, and nothing
would cost you 
dearly"""
print(saa)
print(len(saa))
print()
print()
hell = "Hellow everyone"
print(hell[1:6])
print(hell[-1])
print(hell[::-1])
print()

hello = hell.upper()
print(hello[::-1])
if hello.lower != 'hello!':
    print("Go away!")

if not hello.islower():
    print('I see that you have chosen a side')
print()

print('Helooo'.upper().isupper())
# isalpha(), isalnum(), isspace(), isdecimal(), istitle() also exist
print()
print('This Is A Title Statement: ' + str('This Is A Title Statement'.istitle()))
print('This was not a title statement'.title())
print()
print('Hello starts with H: ' + str('Hello starts'.startswith('Hell')))
print('Hello ends with ello: ' + str('Hello ends with ello'.endswith('ello')))
print()
print()

# join() joins a list of strings with a string between each list element
print(' eats '.join(['cat', 'bat', 'rat']))
print('\t\t'.join(['cat', 'bat', 'rat']))
print(', '.join(['cat', 'bat', 'rat']))
print()
print()
# split() does the opposite by splitting an entire string into a list based on a character/sub-string
print('Ma name est Simon'.split())
print('Mon name est Simon'.split('n'))
print()
print()

#ljust() and rjust() adjusts the total length of the string to the specified number by adding spaces to left
# and right side. center() does the work of both
print('Hello'.rjust(10))
print('Bye'.rjust(88))
print('Bye again'.ljust(40, 'a'))
print('Goodbye, fr.'.center(50, '#'))
print()

# strip(), lstrip() and rstrip() strips strings of whitespaces or specific characters
spam = '      helloxxxxx'
print(spam.lstrip(''))
print(spam.rstrip('x'))
print(spam.strip())
print(spam.strip().rstrip('x'))
print()

# this thing replaces a substring with another string
spam = 'Henlo everyone!'
print(spam.replace('e', 'HAHAHAH'))
print()
print()
print()

# This module copies and pastes texts to/from clipboard
import pyperclip
pyperclip.copy("I am done")     # The text is copied to the clipboard where you can paste it anywhere else
e = pyperclip.paste()           # The copied text in clipboard is pasted to variable e
print(e)
