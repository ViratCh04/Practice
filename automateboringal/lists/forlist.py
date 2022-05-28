for i in range(2):
    print("This is a normal for loop")

print()
print("looping a list")
for i in [1, 2, 3]:
    print(i)

print()
print("Making an artificial list")
fake = list(range(0, 100, 2))
print(fake)


print()
print("Printing a list---------")
stationary = ['pen', 'pineapple', 'apple', 'pencil']
for i in range(len(stationary)):
    print("Index " + str(i) + " in stationary is: " + stationary[i])


print()
print("-------Multi assignment with python--------------")
cat = ['fat', 'orange', 'loud']
size = cat[0]
color = cat[1]
disposition = cat[2]
print(size, color, disposition)

print()
# Much better!!
a, b, c = cat
print("Using multi variable assignment saves up on a lot of redundancy-")
print(a, b, c)

print()
print("----------Swapping variables--------")
a = 1
b = 2
print("Before swap")
print(a, b)
# TADA!
a, b = b, a
print("After swap")
print(a, b)


print()
print("-------------Augmented Assignment operators(or, well, shorthands..?)---------")
a *= 20
print(f"a *= 20 gives: {a}")
a %= 3
print(f"a %= 3 gives: {a}")

