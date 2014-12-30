#!/usr/bin/python
"""
Author: Denis Karanja,
Institution: The University of Nairobi, Kenya,
Department: School of Computing and Informatics, Chiromo campus
Email: dee.caranja@gmail.com,
Task: 30(Digit fifth power)
License type: MIT :)
Status: COMPLETED...
"""
import time
def fifth_power(limit):
	""""Returns the sum of all numbers that can be written as the sum of their digits fifth powers"""
	numbers, sum_numbers, new_sum, values = [], 0, 0, []
	for x in xrange(2, limit):
		numbers.append(x)

	for j in numbers:
		for k in str(j):
			sum_numbers += int(k)**5

		if sum_numbers == j:
			values.append(j)
			new_sum += j
			sum_numbers = 0

		sum_numbers = 0

	return (values, new_sum)

start = time.clock()
print fifth_power(200000)
print "Run time...{}(secs)".format(round(time.clock()-start, 5))