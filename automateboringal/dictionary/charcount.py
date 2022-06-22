# Optional lines in comments
# import pprint
message = 'lsjdojfwlnflsdjlkf we fojflkwe nwenmrljwerj weorr ewrnoqwlwkjrlk423j 4lk23 4lk32jl4kj23lk4 324k 32lk4j32k4oweflksjoiafownja;aj fhdsjsfkasnl fwnlf wej owenflkssniqo'
count = {}

print('Counting occurences of all characters in a string with dictionaries')
for character in message: 
    count.setdefault(character, 0)       # Sets default value for a key in dictionary. Can be also used to add keys
    count[character] = count[character] + 1

print(count)

# pprint.pprint(count)  # Prints the dictionary values in a clean ordered manner
# ordered_dict = pprint.pformat(count) # returns the string values of the output from above line
# print(ordered_dict)