import re

# you can use groups with parentheses in regex
message = 'My mobile number is +91 9340480323'

phonenumregex = re.compile(r'(\d\d) (\d{10})')
mo = phonenumregex.search(message)

# Prints the first and second groups in text
print(mo.group(1))
print(mo.group(2))

# they both print the entire matched text
print(mo.group())
print(mo.group(0))

print('Matching Parentheses with backslash character "\\" ')
# Adding a backslash before the opening and closing parentheses is only exclusive to parentheses.
# Does not work with other symbols. guess we will look into those later
msg = 'My number is (93) 2342390385'
phonenumregex = re.compile(r'\(\d\d\) \d{10}')
mo = phonenumregex.search(msg)

print(mo.group())

print('This section illustrates the use of pipe character | ')

msg1 = 'Batman sux'
msg2 = 'batmobile looks smooth'
msg3 = 'batcopter is what again?'

# if any of the strings contained in parentheses is encountered alongside 'bat, the match pattern will be found
# Lets you match any one group of many groups in a text
batregex = re.compile(r'bat(man|woman|copter|mobile)')

mo = batregex.search(msg1)
if mo == None:
    print('Is the first string non matching?:' +str(True))

mo = batregex.search(msg2)
print(mo.group())

mo = batregex.search(msg3)
print(mo.group())
