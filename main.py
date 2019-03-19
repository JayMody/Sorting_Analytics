##### IMPORTS #####
import algorithims
import data
import csv
import time
import numpy as np

# Because MojaveOS >:(
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt


##### READ FROM FILE #####
with open('data/unique_random.csv') as f:
	reader = csv.reader(f)
	data = list(reader)


##### SORT #####
algorithim_list = [
	algorithims.bubbleSort, 
	algorithims.insertionSort, 
	algorithims.selectionSort,
	algorithims.pythonSort
]

##### ALGORTHIM EVALUATOR #####
for algorithim in algorithim_list:
	sizes = [] # contains size of each array
	times = [] # contains time taken to sort array


	# for each of the arrays in data
	for line in range(len(data)):
		sizes.append(line + 1) # adds arr size to sizes
		start_time = time.time() # start timer

		# Sort array
		arr = np.asarray(data[line], dtype = np.uint16)
		arr_sorted = algorithim(arr)

		times.append(time.time() - start_time) # measures time taken to sort
		print("[{}] ".format(algorithim.__name__), line, "/{}".format(len(data)), end = '\r') # prints the current dataset being evaluated


	# Total time taken for an algorithim
	print("[{}]    Time (s): ".format(algorithim.__name__), np.sum(times))


	# Plots time size relationship
	plt.plot(sizes, times, label = algorithim.__name__)


	##### WRITE TO FILE #####
	with open('data/{}.csv'.format(algorithim.__name__), 'a') as f:
		writer = csv.writer(f)
		writer.writerows([sizes, times])



##### Final graph drawn and saved #####
plt.legend(loc = 'upper left')
plt.draw()
plt.savefig('fig.png')
