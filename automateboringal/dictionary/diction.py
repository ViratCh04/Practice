cat = {'size' : 'chonk', 'color' : 'white', 'disposition' : 'wild'}
print(cat['size'])
print('My cat has ' + cat['color'] + ' fur')
print('size' in cat)
print('size' not in cat)
print('Is the chonk in dictionary?')
print('chonk' in cat.values())


print()
print(list(cat.keys()))
print(list(cat.values()))
print(list(cat.items()))
print()
print('Printing Dictionary items like a normal human without the list conversion now')
# dict.items() actually returns tuples of key value pairs
print(cat.items())

print()
print()
print("Printing values in dictionary")
for v in cat.values():
    print(v)

print()
print("Printing key-value pairs in dictionary")
for k,v in cat.items():
    print(k, v)

print('Assigning tuples to a single variable')
for v in cat.items():
    print(v)

# dict.get()
print()
print()
if 'age' not in cat:
    print('No age key in cats')
print()
print('Using get method with dictionaries is much less verbose than using an if statement (Provides a fallback default value if the particular key does not exist in dictionary instead of slamming down a KeyError), else, returns the value/s associated with the key')
print(cat.get('size', 'NO SIZE') + ' is the size')
print(cat.get('age', 'No age'))

# dict.setdefault()
if 'age' not in cat:
    cat['age'] = 0
print()
print('Using if statements to set a value which does not exist is, again, redundant. So we have setdefault()')
cat.setdefault('species', 'cat')
print(cat.items())
