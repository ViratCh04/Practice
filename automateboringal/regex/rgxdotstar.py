import re

# The carat character ^ means that the string must start with that pattern
beginwhelloregex = re.compile(r'^hello')
# Not including the match object anymore cuz time consuming, understand the output by yourself
mo1 = beginwhelloregex.search('hello world!')
print(mo1.group())
print()

# The dollar character $ makes sure that the string must end with that pattern
endwhelloregex = re.compile(r'world!$')
print(endwhelloregex.search('hello world!'))
print("When string ends with some other pattern($), match not found = ", end = "")
print(endwhelloregex.search('hello world!FSDLJFWLJF') == None)
print()

# If the regular expression has both ^ and $ ie ^(insertpatternhere)$
# That means that the string must be matching to (insertpatternhere)
alldigitsregex = re.compile(r'^\d+$')
print(alldigitsregex.search('9834048020932'))
print("when string differs from the regular expression(^(lala)$) by even a single character, match not found = ", end = "")
print(alldigitsregex.search('9434390d4340') == None)
print()

#---------------
print("the dot (.) character")
msg = 'the fat cat with a hat sat on a flat mat'
# The dot . character matches anything except newlines
atregex = re.compile(r'.at')
print(atregex.findall(msg))

print("Will include any two characters before at(will also include spaces from now on)")
atregex = re.compile(r'.{1,2}at')
print(atregex.findall(msg))

print("using dot . char with * star character, you mean that any pattern can be there")
print("Extracting the first and last name from a database")
nameregex = re.compile(r'First name: (.*) Last Name: (.*)')
#returns a list of tuples containing the name of a person
print(nameregex.findall('First name: Virat Last Name: Chauhan'))


serve = '<human serve> for dinner yum>'
print("Greedy and Non-greedy matching(with ?) on .* regex\n Non - greedy matching picks minimum possible characters from the string")
nongreedymatch = re.compile(r'<(.*?)>')
print(nongreedymatch.findall(serve))
print("Greedy matching picks the combination with maximum possible characters from the string")
greedymatch = re.compile(r'<(.*)>')
print(greedymatch.findall(serve))

robocop = 'secure.\ncontain.\nprotect.'
print("the code below prints the pattern until it encounters newline")
dotstar = re.compile(r'.*')
print(dotstar.search(robocop))
print("re.DOTALL(used with re.compile) makes sure that the . in regex includes the newline operator as well")
dotstar = re.compile(r'.*', re.DOTALL)
print(dotstar.search(robocop))


test = 'Ok, Today has been a quick-sort(bad pun intended) of a day but I think it Is Okay to say that Atleast its been productive'
print("Testing re.IGNORECASE / re.I(used with re.compile) to ignore uppercase/lowercase while pattern matching")
vowelregex = re.compile(r'[aeiou]')
print(vowelregex.findall(test))

print("using re.I/re.IGNORECASE now to make pattern matching case-insensitive")
vowelregex = re.compile(r'[aeiou]', re.IGNORECASE)
print(vowelregex.findall(test))
