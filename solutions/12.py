#!/usr/bin/python
"""
Author: Denis Karanja,
Institution: The University of Nairobi, Kenya,
Department: School of Computing and Informatics, Chiromo campus
Email: dee.caranja@gmail.com,
Task: 12(What is the value of the first triangle number to have over five hundred divisors?)
License type: MIT :)
Status: PENDING...
"""
import time

def recursive_tri(nth_term):
	"""A recursive triangle numbers finder"""
	if nth_term == 1 or nth_term == 0:
		return nth_term
	else:
		return  nth_term + recursive_tri(nth_term - 1)

def iterative_tri(num):
	"""An iterative triangle number finder"""
	num_sum = 0
	for i in xrange(1, num+1):
		num_sum += i
	return num_sum

def factors_count(tri_num):
	"""Returns the number of factors tri_num has"""
	factors, i = 0, tri_num
	while i > 0:
		if tri_num % i is 0:
			factors += 1
			i -= 1
		else:
			i -= 1
	return factors

def greatest_factor(limit, factors, i = 500):
	print "Calculating the first triangle number with > {} divisors...".format(factors)
	while i <= limit:
		tri_num = iterative_tri(i)
		if factors_count(tri_num) > factors:
			return (i, tri_num)
		elif i is limit:
			limit += 1
		i += 1

startTime = time.clock()
print greatest_factor(100000, 50)
done = time.clock() - startTime
print "Run time... {}(secs) or {}(mins)".format(round(done, 5), round(done / 60, 5))


