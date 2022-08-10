import re

msg = 'Office - +91 9102919255, Home - +91 9338185761'

# using the search function with regex object which returns a match object only works if you are looking for the
# First match. However this is pretty much useless if you want all of the matches carrying the format in regex object
# To do this, we have the findall() function to work with, which returns all of the matches
phoneregex = re.compile('\+\d\d \d{10}')
print("Printing a list of strings")
print(phoneregex.findall(msg))

# If there are 2 or more than 2 grps, a list of tuples of strings(matching grps) is returned via findall()
phoneregex = re.compile('(\+\d\d) (\d{10})')
print("Printing a list of tuples (only possible if there are atleast 2 groups")
print(phoneregex.findall(msg))

phoneregex = re.compile(r'((\+\d\d) (\d{10}))')
print("Printing two groups(as tuples) within another group")
print(phoneregex.findall(msg))

# There are three/six character classes/shorthands I should be aware of
# \d- any digit from 0 to 9; \D- any character that is not a digit from 0 to 9
# \w- any character that is a letter, numeric digit, underscore; \W- any character not lying in \w's range
# \s- Any space, tab, or newline character; \S- any character that doesn't lie in \s

print("Using \s and \w")
lyrics = '12 Drummers Drumming 11 Pipers Piping 10 Lords a Leaping 9 Ladies Dancing 8 Maids a Milking 7 Swans a Swimming 6 Geese a Laying 5 Golden Rings 4 Calling Birds 3 French Hens 2 Turtle Doves and 1 Partridge in a Pear Tree'

xmasregex = re.compile(r'\d+\s\w+')
print(xmasregex.findall(lyrics))

print("Prints all words in song")
xmasregex = re.compile(r'\d*\s\w+')
print(xmasregex.findall(lyrics))


# We can make our own character classes by encasing them in square brackets []

msg = 'Batman is taking a biiiiiiiiig dump'
vowelregex = re.compile(r'[aeiouAEIOU]')            # similar to a|e|i|o|u|(caps) but less verbose
print(vowelregex.findall(msg))

print("more combinations with custom character classses: ")
print("prints characters from a-f and A-F")
testregex = re.compile(r'[a-fA-F]')
print(testregex.findall(msg))

# The carat character ^ is used to make negative character classes,
# This will exclude any range passed in the raw string, making it essentially an opposite of character class
print("Testing ^ in regular expressions")
consonantregex = re.compile(r'[^aeiouAEIOU ]')
print(consonantregex.findall(msg))

