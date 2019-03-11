##### Bubble Sort #####
def bubbleSort(arr):
	isSorted = False
	for i in range(len(arr)):
		isSorted = True
		for i in range(len(arr) - i - 1):
			if (arr[i] > arr[i+1]):
				arr[i], arr[i+1] = arr[i+1], arr[i]
				isSorted = False
		if (isSorted == True):
			break
	return arr

##### Insertion Sort #####

##### Selection Sort #####