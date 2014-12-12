#!/usr/bin/python
"""
Author: Denis Karanja,
Institution: The University of Nairobi, Kenya,
Department: School of Computing and Informatics, Chiromo campus
Email: dee.caranja@gmail.com,
Task: 5(A number that is divisible by numbers 1 through 20. eg 2520 is divisible by numbers 1 thru 10)
License type: MIT :)
Status: PENDING...
"""
import time
startTime = time.clock()

"""def recursive_fibo(num):
	if num == 1 or num == 0:
		return num
	else:
		return recursive_fibo(num - 1) + recursive_fibo(num - 2)"""

def iterrativeFibo(num):
	x = i = 0
	y = z = 1
	for i in range(0, num+1):
		x = y
		y = z
		z = x + y
	return x

print "Calculating using itterative fibonacci. Please wait..."
print "\tUsing itterative {}".format(iterrativeFibo(10))
iterrative_time = time.clock() - startTime
print "\tRun time... %.5f(secs) or %.5f(mins)" % (iterrative_time, (iterrative_time / 60.0))

"""
print "\nCalculating using recursive fibonacci. Please wait..."
print "\tUsing recursion {}".format(recursive_fibo(11))
recursive_time = time.clock() - startTime - iterrative_time
print "\tRun time... %.5f(secs) or %.5f(mins)" % (recursive_time, (recursive_time / 60.0))
"""