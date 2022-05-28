print(list('hello'))

name = 'Sophia'
print()
print(name[0])
print(name[1:4])
print(name[-2])
print(name[5:])
print("Q. Is string 'ph' in variable 'name'? ")
if 'ph' in name:
    print(True)

print()
print('Printing string through for loop')
for letter in name:
    print(letter, end=' ')
print()
print()

# Strings in Python are immutable
# Thus, to modify a string, we copy it using slicing and insert the changes
nom = 'Harry the Harold'
print(nom)
new_name = nom[0:6] + 'a' + nom[9:16]
print('New name after modifying nom is : ' + new_name)
print()
print()

# When you copy a list to a variable, You really only pass a reference to that list in memory to the variable.
# Thus, any changes made to the copy of the list are also reflected back to the original list as they are one and the same
spam = [1, 2, 3, 4, 5]
man = spam
man[0] = "Mario"
print("list man[]: ")
print(man[:])
print("list spam[]: ")
print(spam[:])
print("These lists are one and the same. As lists are mutable, you do not store them inside the variable directly. You just store the references to the list in memory")
# This holds true for all mutable values, you always store the references to them instead of the data type itself.
# And, all changes done to any number of copies of the variable of mutable data types are reflected to the data type itself
# The whole references thing exists as a tradeoff as while handling huge amounts of data, copying lists every time will
# be hard on memory. And references truly shine in such a scenario.
# Immutable values like strings and tuples do not have this problem as they cannot be modified in the place


print()
print()
print()
print("Copying lists through 'copy' module's function 'deepcopy()'")

import copy
cheese = [1, 2, 3, 4, 5, 6]
butter = copy.deepcopy(cheese)
butter[1] = "LOL"
butter[2] = "Ben 10"
print("cheese[]:", end=' ')
print(cheese[:])
print("butter[]:", end=' ')
print(butter[:])
print()
print()

# You can continue typing list values in multiple lines with proper indentations
spem = ['yuuki',
        'fuuji',
        'yamashi']
# You can use the slash('\') character to continue the print statement in the next line while ignoring indentations

print('One year ago, ' + \
        'I was alive')