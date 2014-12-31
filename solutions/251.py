#!/usr/bin/python
"""
Author: Denis Karanja,
Institution: The University of Nairobi, Kenya,
Department: School of Computing and Informatics, Chiromo campus
Email: dee.caranja@gmail.com,
Task: 251(Cardano tripplet)
License type: MIT :)
Status: COMPLETED...
"""
import time
def cardano_triplet(limit):
	cardano, cardano_trips = 0, []
	for a in xrange(1, limit+1):
		for b in xrange(1, limit+1):
			for c in xrange(1, limit+1):
				l = a + b*pow(c, 0.5)
				r = a - b*pow(c, 0.5)
				left = float(str(pow(abs(l), (1./3))))
				right = float(str(pow(abs(r), (1./3))))
				a_b_c = a + b + c
				if left - right == 1.0 and a_b_c <= 1000:
					#print (a, b, c), left - right
					cardano += 1

	return cardano

start = time.clock()
print "Finding cardano triplets..."
print cardano_triplet(100)
print "Run time... {}(secs)".format(round(time.clock() - start, 5))
