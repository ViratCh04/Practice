
lest = ['cat', 'bat', 'rat', 'fat', 'mat']
num = [[10, 20, 40, 50, 60], [1, 2, 3, 4, 5]]

# Demonstrates negative indices
for i in range(-1, -6, -1):
    print(lest[i])

print()
print('The ' + lest[-3] + ' is afraid of the ' + lest[-5])

print()
# Slices in lists
print(lest[1:4])
print(lest[:2])
print(lest[1:])
print(lest[:])

print("Inserting into lists with slicing")
lest[1:1] = ['pat', 'sat', 5]
print(lest[:])

print("deleting list elements")
del lest[3]
del lest[2]
print(lest[:])

print()
print("length of list [1, 2, 3] is " + str(len([1, 2, 3])))
print("length of list lest[] is " + str(len(lest)))
print()
print("printing string 'hello' as a list: ")
print(list("hello"))

print("multiplying list lest[] by 3 times....")
print(lest[:] * 3)


print("Demonstrating 'in' and 'not in' operator")
if 'sat' not in lest:
    print("sat does not exist in lest[]")
if 'rat' in lest:
    print("rat exists in lest[]")

    