def mergeSort(a: list[int], p:int, r: int):
	if p < r:
		q = p + (r - p)//2
		mergeSort(a, p, q)
		mergeSort(a, q + 1, r)
		merge(a, p, q, r)

def merge(a: list[int], p: int, q: int, r: int):
	n1 = q - p + 1
	n2 = r - q

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

	# copy remaining elements from arrays
	while i < n1:
		a[k] = m[i]
		i += 1
		k += 1
	
	while j < n2:
		a[k] = n[j]
		j += 1
		k += 1

def binarySearch(a: list[int], l: int, h: int, difference: int):
	while(l <= h):
		m = l + (h - l)//2
		if a[m] == difference:
			return m
		
		if a[m] < difference:
			l = m + 1

		else:
			h = m - 1

def main():
	a = [23, 19, 21, 88, 11, 8, 5, 1, 22]
	mergeSort(a, 0, len(a) - 1)
	print("Sorted array is: \n" + str(a))
	sum = int(input("Enter the number whose sum you wish to find:"))
	for i in range(0, len(a)):
		index = binarySearch(a, 0, len(a) - 1, sum - a[i])
		if (index != None and index != i):
			print(f"Match found at {i} and {index}")
			return
	print("Match not found")

if __name__ == "__main__":
	main()