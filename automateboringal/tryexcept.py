def division(divideby):
    try:
        return 99 / divideby
    except ZeroDivisionError:
        return 'Error: You cannot divide a number by zero'

print(division(9))
print(division(10))
print(division(0))
print(division(88))


print("How many cats do you have?")
cats = input()
try:
    if int(cats) < 0:
        print("byeeeeeeeeeeeeee")
    elif int(cats) >= 4:
        print("You have got way too much fluff")
    else:
        print("Not that many cats eh")
except ValueError:
    print("Enter a number")