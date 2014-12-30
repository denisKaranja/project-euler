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
def cardano_triplet(limit):
	cardano, cardano_trips = 0, []
	for a in xrange(1, limit+1):
		for b in xrange(1, limit+1):
			for c in xrange(1, limit+1):
				cardano_trips.append((a, b, c))

	return cardano_trips



print "Finding cardano triplets..."
print cardano_triplet(10)
