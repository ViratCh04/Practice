def bubbleSort(a: list[int]):
    for i in range(0, len(a)):
        for j in range(0, len(a) - i - 1):
            if a[j] > a[j + 1]:
                temp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp            

def main():
    a = [23, 19, 21, 88, 11, 8, 5, 1, 22]
    print(a)
    bubbleSort(a)
    print(a)

if __name__ == "__main__":
    main()