#!/usr/bin/python
"""
Author: Denis Karanja,
Institution: The University of Nairobi, Kenya,
Department: School of Computing and Informatics,
Email: dee.caranja@gmail.com,
Euler project solution = 250(250250 ->> sum whose elemets is divisible by 250 {1^1, 2^2, 3^3...250250^250250}.)
give the last 16 digits
Status.. PENDING...
"""
import time
calls = 0

def selfPower(num):
	if num == 1:
		return 1
	else:
		return num**num + selfPower(num - 1)


def revised_self_power(num, list_sum = 0):
	for i in xrange(1, num+1):
		list_sum += i**i
	return list_sum

start = time.clock()
print "{}".format(revised_self_power(999))
print "Run time..{}secs".format(round(time.clock()-start, 5))
