import re

# The metacharacter ? only finds a match if the group preceding this character is repeated zero or one time
# that is, it is used to find an optional group in the string
print("? metacharacter at work:")
batregex = re.compile(r'Bat(wo)?man')
mo = batregex.search("adventures of Batman")
print(mo.group())
# The matching string is printed regardless of whether it contains 'wo' in it or not
mo = batregex.search("adventures of Batwoman.")
print(mo.group())
# If the optional group is found, the string will be printed

# ? works with all sorts of characters
phoneregex = re.compile(r"(\d\d\d-)?\d\d\d-\d\d\d\d")
mo = phoneregex.search("My phone number is 342-221-3803")
print(mo.group())

mo = phoneregex.search("My phone number is 444-4902")
print(mo.group())

#-------------
print("* metacharacter at work")
# * metacharacter only finds a match if the group preceding this character is repeated zero or more times
# Essentially a better ? metachar but honestly depends on your usage requirements
batregex = re.compile(r'Bat(wo)*man')
mo = batregex.search("adventures of Batwoman")
print(mo.group())

mo = batregex.search("adventures of Batwowowowowowowowowowowowowowowowowoman")
print(mo.group())


#---------------------------------
print("+ metacharacter at work")

# + character only finds a match if the group preceding this character is matching atleast one or more times
# works when you need the group to repeat atleast one time with no limit
batregex = re.compile(r'Bat(wo)+man')
mo = batregex.search("adventures of Batman")
print("For 'adventures of batman'-")
print("match not found: " +str(mo == None))

mo = batregex.search("adventures of Batwoman")
mo1 = batregex.search("adventures of Batwowowowowowowowowoman")
print(f"{mo.group()}\n{mo1.group()}")


#------------------------------------
print("Checking for symbols with backslashes")
# Clearly, we cannot look for + ? and * simply if we want to search for them in a text
# Thus, we use \+ and \? and \* 
patternregex = re.compile(r'\+\?\*')
mo = patternregex.search("imma study +?* kbye")
print(mo.group())

# Looks for multiple matches for the raw string
patternregex = re.compile(r'(\+\?\*)+')
mo = patternregex.search("imma study +?*+?*+?*+?*+?*+?* kbye fr")
print(mo.group())



#----------------------------------------
print("Matching for specific repetitions with curly braces {}")
# If you have a group that you want to repeat a specific number of times,
# follow the group in your regex with the number in curly brackets.
haregex = re.compile(r'(ha){3}')
mo = haregex.search("hahahaha joke's on you pal")
print(mo.group())

# Checks for optional commas, spaces and a total repetition of three phone numbers
haregex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?( )?){3}')
mo = haregex.search("my numbers are 324-284-2458, 501-3043,098-830-0931")
print(mo.group())



print("Curly braces with maximum and minimum repeats")
# You can set the maximum or minimum number of repetitions for a particular group by
# setting a range.
haregex = re.compile(r'(ha){3,5}')
mo = haregex.search("hahaha")
print(mo.group())
#prints four ha's
mo = haregex.search("hahahaha")
print(mo.group())
# prints five ha's
mo = haregex.search("hahahahaha")
print(mo.group())

# Sets an indefinite maximum number of ha's for matching
haregex = re.compile(r'(ha){3,}')
mo = haregex.search("hahahahahahahahahaha")
print(mo.group())

print("Greedy and Non-greedy matching(with ?)")
haregex = re.compile(r'\d{3,5}')
# If the total number of repetitions in the string to be checked is equal or greater to the maximum repeats in range,
# By default, the maximum number of repeated groups is matched and returned
# This type of matching is called Greedy matching
mo = haregex.search("303940432")
print(mo.group())
# To set the group repetitions to minimum in the braces range by default, 
# We use the ? operator once again, where the ? character has a wholly different function
# This type of matching with a ? succeeding the range is called Non-Greedy matching
haregex = re.compile(r'\d{3,5}?')
mo = haregex.search("930940389403")
print(mo.group())

