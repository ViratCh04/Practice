# The scripts for searching text patterns without non regular expressions are very long
# To make the code shorter, we will use the 're' module
import re

message = 'call me at 415-333-4345, or at 325-555-9999 at office line'

# the r in the beginning is just to ensure that the string is treated as a raw string
# such that no special sequence is executed
# Since regular expressions frequently use backslashes in them, 
# it is convenient to pass raw strings to the re.compile() function instead of typing extra backslashes.

# Passing a string value representing your regular expression to re.compile() returns a Regex pattern object (or simply, a Regex object).

# To create a Regex object that matches the phone number pattern, enter the following into the interactive shell. 
# (Remember that \d means “a digit character” and \d\d\d-\d\d\d-\d\d\d\d is the regular expression for the correct phone number pattern.)
Phonenumregex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# Checks for three characters like letters, numbers and underscore
heyregex = re.compile(r'\w{3}')

# A Regex object’s search() method searches the string it is passed for any matches to the regex. 
# The search() method will return None if the regex pattern is not found in the string. 
# If the pattern is found, the search() method returns a Match object. 
# Match objects have a group() method that will return the actual matched text from the searched string.
matchobject = Phonenumregex.search(message)
print(matchobject.group())
print(Phonenumregex.findall(message))

# or, there is a simpler way instead of creating a match object
# This returns all the matched texts from the searched string
print(heyregex.findall('today is the day that i turn my hay, once i do get flayed, I will say, come, jump into the way'))