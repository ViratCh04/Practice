# only works on sorted lists
def binarySearch(a, item, low, high):
    while(low <= high):
        mid = low + (high - low)//2

        if a[mid] == item:
            return mid
        
        if a[mid] < item:
            low = mid + 1
        
        else:
            high = mid - 1

    return -1

def main():
    a = [10, 20, 30, 40, 50, 60, 70, 80, 900]
    print("This is Binary Search")
    item = int(input("Enter item to search: "))

    index = binarySearch(a, item, 0, len(a) - 1)
    if index == -1:
        print("Match not found")
    else:
        print("Match found at index " + str(index))

if __name__ == "__main__":
    main()