##### IMPORTS #####
import csv
import time
import numpy as np

##### SORT ALGORITHIMS #####
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

##### READ FROM FILE #####
with open('data/unique_random.csv') as f:
	reader = csv.reader(f)
	data = list(reader)

##### SORT #####
stime = time.time()
for line in range(len(data)):
	arr = np.asarray(data[line], dtype = np.uint16)
	data[line] = bubbleSort(arr)
print(time.time() - stime())

##### WRITE TO FILE #####
with open('result.csv', 'w') as f:
	writer = csv.writer(f)
	writer.writerows(data)


