def mergeSort(a: list[int], p: int, r: int):
	if p < r:
		q = p + (r - p)//2
		mergeSort(a, p, q)
		mergeSort(a, q + 1, r)
		merge(a, p, q, r)

# the merge algorithm in third edition of clrs is outdated, the 4th edition's algorithm works fine
def merge(a: list[int], p: int, q: int, r: int):
	n1 = q - p + 1
	n2 = r - q
	# declaring temporary arrays to store parts of original array
	(m, n) = ([0] * n1, [0] * n2)
	for i in range(0, n1):
		m[i] = a[p + i]
	for j in range(0, n2):
		n[j] = a[q + j + 1]
	
	(i, j, k) = (0, 0, p)

	while i < n1 and j < n2:
		if m[i] <= n[j]:
			a[k] = m[i]
			i += 1
		else:
			a[k] = n[j]
			j += 1
		k += 1
		
	# Copy the remaining elements of m[], if there are any
	while i < n1:
		a[k] = m[i]
		i += 1
		k += 1
 
    # Copy the remaining elements of n[], if there are any
	while j < n2:
		a[k] = n[j]
		j += 1
		k += 1


def main():
	a = [23, 19, 21, 88, 11, 8, 5, 1, 22]
	print("Unsorted array is: \n" + str(a))
	mergeSort(a, 0, len(a) - 1)
	print("Sorted array is: \n" + str(a))

if __name__ == "__main__":
	main()