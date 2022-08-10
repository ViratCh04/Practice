import re

message = 'Ardent Larry sent the document to Ardent Harry'
nameregex = re.compile(r'Ardent \w+')
print(nameregex.findall(message))
# We can swap the regular expression patterns found in the string with any other string
# With the help of sub() method whic substitutes the re with its first argument
print('Using reobject.sub() now to substitute the confidential names:')
subbed = nameregex.sub('REDACTED', message)
print(subbed)

print('We can also print out a single character included in a group with findall():')
nameregex = re.compile(r'Ardent (\w)\w+')
print(nameregex.findall(message))

print('Can also print out the first group in regular expression: ')
# Here, \1 implies the first group, ie., (\w). The names are replaced by Agent and the first group(which is the first letter of their names)
# followed by asterisks
subbed = nameregex.sub(r'Agent \1***', message)
print(subbed)

print() 
print()
print('''re.VERBOSE lets us add documentation for large and complicated regular expressions as it ignores any whitespaces so you can add any comments to explain what is going on''')
print()
phoneregex = re.compile(r'''(
                ( \d{3}- |          # area code(without parentheses, with dash)
                  \(\d{3}\))       # "or" area code(with parentheses, w/o dash)
                \d{3}             # first three digits
                (-)                 # second dash
                \d{4}          # last 4 digits
                )''', re.VERBOSE)

print(phoneregex.findall('call me at 415-333-4345, or at 325-555-9999 at office line'))

print()
print("You can also add multiple arguments to re.compile using bitwise operator |:")

print("for example, re.compile('bla bla', re.I | re.DOTALL | re.VERBOSE)")