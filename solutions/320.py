#!/usr/bin/python
"""
Author: Denis Karanja,
Institution: The University of Nairobi, Kenya,
Department: School of Computing and Informatics, Chiromo campus
Email: dee.caranja@gmail.com,
Task: 320(Factorials divisible by a huge int)
License type: MIT :)
Status: PENDING...
"""
import time

def factorial(num):
	"""An iterative fibonacci number finder"""
	product = 1
	for i in xrange(num):
		product *= (i + 1)
	return product


start = time.clock()
print factorial(5)
print "Run time...{}(secs)".format(time.clock()-start)
