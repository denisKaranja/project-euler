#!/usr/bin/python
"""
Author: Denis Karanja,
Institution: The University of Nairobi, Kenya,
Department: School of Computing and Informatics, Chiromo campus
Email: dee.caranja@gmail.com,
Task: 5(A number that is divisible by numbers 1 through 20. eg 2520 is divisible by numbers 1 thru 10)
License type: MIT :)
Status: COMPLETED...
"""
import time

# def is_divisible(limit):
# 	number = limit
# 	print "Calculating a number that is divisible by 1 through {}...".format(limit)
# 	while not all((number % n == 0) for n in xrange(2, limit+1)):
# 		number += 2
# 	return number

# print "\tNumber found->> {}" .format(is_divisible(20))
#print "\tRun time... %.5f(secs) or %.5f(mins)" % (time.clock() - startTime, ((time.clock() - startTime) / 60.0))

"""Revised version of the problem"""
def gcd(a, b):
	"""Finds the gcd of two numbers"""
	while b is not 0:
		(a, b) = (b, a%b)
	return a

def lcm(a, b):
	"""Returns the lcm of a number"""
	return (a*b)/ gcd(a, b)

startTime = time.clock()
print reduce(lcm, range(1, 21))
print "Run time...{}(secs)".format(round(time.clock() - startTime, 5))

