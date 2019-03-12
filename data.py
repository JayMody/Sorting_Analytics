import csv
import random
import time

##### Unique Random #####
def unique_random(max_val):
	unique_random = []
	for i in range(1, max_val + 1):
		unique_random.append(random.sample(range(0, i), i))

	return unique_random

##### Uniform Random #####
def uniform_random(max_val):
	uniform_random = []
	for i in range(1, max_val + 1):
		uniform_random.append([random.randint(0, i - 1) for j in range(i)])

	return uniform_random

def reverese_order(max_val):
	reverse_list = []
	for i in range(1, max_val + 1):
		reverse_list.append([j for j in range(i, 0, -1)])
	
	return reverse_list

##### Write To Text File #####
n_samples = 500

samplers = [unique_random, uniform_random, reverese_order]
for sampler in samplers:
	stime = time.time()
	data = sampler(n_samples)

	with open("data/{}.csv".format(sampler.__name__), "w") as f:
		writer = csv.writer(f)
		writer.writerows(data)

	print(time.time() - stime)