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
startTime = time.clock()

def is_divisible(limit):
	number = limit
	print "Calculating a number that is divisible by 1 through {}...".format(limit)
	while not all((number % n == 0) for n in xrange(2, limit+1)):
		number += 2
	return number

print "\tNumber found->> {}" .format(is_divisible(20))
print "\tRun time... %.5f(secs) or %.5f(mins)" % (time.clock() - startTime, ((time.clock() - startTime) / 60.0))
#232792560