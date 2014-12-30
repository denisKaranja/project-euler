#!/usr/bin/python
"""
Author: Denis Karanja,
Institution: The University of Nairobi, Kenya,
Department: School of Computing and Informatics, Chiromo campus
Email: dee.caranja@gmail.com,
Task: 32(Pandigital products eg 7254 = 39*186-->all pandigital 1..9)
License type: MIT :)
Status: PENDING...
"""
import time
def pandigital(limit):
	"""Returns the sum of products whose multiplicand/multiplier/product are pandigital 1..9"""
	pand_1_9, pan_sum = 123456789, []
	for a in xrange(1, limit+1):
		for b in xrange(1, limit+1):
			product = a * b
			number = sorted(str(str(product) + str(a) + str(b)))
			number = int("".join(number))
			if number == pand_1_9:
				pan_sum.append(product)
				#print (a, b, product)

	return sum(set(pan_sum))

print "Calculating pandigital product sum..."
start = time.clock()
print pandigital(200)
print "Run time...{}(secs)".format(round(time.clock()-start, 5))
