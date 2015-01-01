#!/usr/bin/python
"""
Author: Denis Karanja,
Institution: The University of Nairobi, Kenya,
Department: School of Computing and Informatics, Chiromo campus
Email: dee.caranja@gmail.com,
Task: 56(Powerful digit sum)
License type: MIT :)
Status: COMPLETED...
"""

def generator(limit):
	"""Generates a list with digit sum of numbers from 1 to limit-1"""
	digit_sum_list = []
	for a in xrange(1, limit):
		for b in xrange(1, limit):
			digit_sum = sum([int(y) for y in str(a**b)])
			digit_sum_list.append((digit_sum, str(a)+"^"+str(b)))

	return max(digit_sum_list)

def main():
	return (generator(100))

if __name__ == "__main__":
	import time
	print("Calculating maximum powerful digit sum...")
	start = time.clock()
	print(main())
	print("Run time...{}(secs)".format(round(time.clock()-start, 5)))