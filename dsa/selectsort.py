def selectionSort(a):
    for i in range(0, len(a) - 1):
        minIndex = i
        for j in range(i+1, len(a)):
            if a[j] < a[minIndex]:
                minIndex = j
        temp = a[i]
        a[i] = a[minIndex]
        a[minIndex] = temp

def main():
    a = [8,3,2,324,3243,22,112]
    print(a)
    selectionSort(a)
    print(a)

if __name__ == "__main__":
    main()

