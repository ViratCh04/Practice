def linearSearch(a, item):
    for i in range(0, len(a)):
        if a[i] == item:
            return i
    return -1

def main():
    a = [234, 2382, 898, 231, 894, 2, 10, 50]
    item = int(input("Enter item to search: "))
    
    index = linearSearch(a, item)
    if index == -1:
        print("Match not found")
    else:
        print("Item found at index " + str(index))

if __name__ == "__main__":
    main()