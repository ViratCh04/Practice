total = 0
for num in range(201):
    total = total + num

print(f"Sum of first 200 numbers is: {total}")

print()
print("Table of 3")
j = 1
for i in range(3, 31, 3):
    print(f"3 x {j} = " + str(i))
    j = j + 1

print()
print("number moonwalk")
for k in range(10, -1, -2):
    print(f"{k}")