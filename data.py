import csv
import random
import time

##### Unique Random #####
def unique_random(max_val):
	unique_random = []
	for i in range(1, max_val):
		unique_random.append(random.sample(range(0, i), i))

	return unique_random

##### Uniform Random #####
def uniform_random(max_val):
	uniform_random = []
	for i in range(1, max_val):
		uniform_random.append([random.randint(0, i - 1) for j in range(i)])

	return uniform_random

##### Write To Text File #####
stime = time.time()
data = uniform_random(100)

with open("data/uniform_random.csv", "w") as f:
	writer = csv.writer(f)
	writer.writerows(data)

print(time.time() - stime)
