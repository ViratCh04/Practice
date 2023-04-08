def insertionSort(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1       # finds the upper limit for sorted right half
        while j >= 0 and a[j] > key:        
            # using key here(in line 5 and line 7) is a must as the next line modifies the value of a[i], 
            # thereby requiring the use of the backup value of a[i] which is stored in key
            a[j + 1] = a[j]         # make space for the value being sorted
            j -= 1
        # store the sorted element in correct position
        a[j + 1] = key

def main():
    a = [234, 322, 3854, 45, 86, 57, 22, 98, 17, 5]
    print("Unsorted list is: \n" + str(a))

    insertionSort(a)
    print("Sorted list is: \n" + str(a))

if __name__ == "__main__":
    main()