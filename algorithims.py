### Bubble Sort ###
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

### Insertion Sort ###
def insertionSort(arr):
	for i in range(1, len(arr)):
		key = arr[i]
		j = i-1
		while j >= 0 and key < arr[j]:
			arr[j+1] = arr[j]
			j -= 1
		arr[j+1] = key
	return arr

### Selection Sort ###
def selectionSort(arr):
	for i in range(len(arr)):
		idx = i
		for j in range(i+1, len(arr)):
			if arr[j] < arr[idx]:
				idx = j
		arr[i], arr[idx] = arr[idx], arr[i]
	return arr

### Python Sort ###
def pythonSort(arr):
	return list.sort(list(arr))

### Merge Sort ###
def mergeSort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2 
        L = arr[:mid]
        R = arr[mid:] 
  
        mergeSort(L) 
        mergeSort(R)
  
        i = j = k = 0
          
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
           
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1