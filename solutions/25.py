#!/usr/bin/python
"""
Author: Denis Karanja,
Institution: The University of Nairobi, Kenya,
Department: School of Computing and Informatics, Chiromo campus
Email: dee.caranja@gmail.com,
Task: 25(1st fibonacci num to contain 1000 digits)
License type: MIT :)
Status: COMPLETED...
"""
import time
startTime = time.clock()

def iterative_fibo(num):
	x = i = 0
	y = z = 1
	for i in xrange(num):
		x = y
		y = z
		z = x + y
	return x

j = 12
print "Calculating..."
while len(str(iterative_fibo(j))) != 1000:
    j += 1

print j
print "Run time...{} secs \n".format(round(time.clock() - startTime, 4))