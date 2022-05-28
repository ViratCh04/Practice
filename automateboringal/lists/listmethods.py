spam = ['hey', 'why', 'bye', 'cry', 'psy']

print(spam.index('cry'))
print(spam.index('bye'))

# append method adds the item to the end of the list, while insert method adds the item to the specified index
spam.append('goose')
spam.insert(1, 'hey')

print(spam[:])

# Unlike del method, remove only needs the value to be removed instead of its index
# But it only deletes the first match it finds, thus if multiple matching values of the same argument exists,
# Only the first value is deleted
spam.remove('hey')
print()
print(spam[:])

# You can sort items in a list whether they are strings or integers, using sort() method
lala = [1, 2.1, 1.1, 209, 5, 100]
print()
print(lala[:])
spam.sort()
lala.sort()
print("sorted lists are")
print(lala[:])
print(spam[:])

print()
print("reverse sort: ")
spam.sort(reverse=True)
print(spam[:])

print()
print()
# Sort automatically sorts the uppercase letters before the lowercase letters. To prevent this, we can
hue = ['a', 'A', 'Z', 'x', 'X']
spam.sort(key=str.lower)
print(spam[:])
