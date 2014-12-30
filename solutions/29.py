#!/usr/bin/python
"""
Author: Denis Karanja,
Institution: The University of Nairobi, Kenya,
Department: School of Computing and Informatics, Chiromo campus
Email: dee.caranja@gmail.com,
Task: 29(Distinct powers)
License type: MIT :)
Status: COMPLETED...
"""
def distinct_powers(limit):
	"""Get the number of distinct powers"""
	powers = []
	for a in xrange(2, limit+1):
		for b in xrange(2, limit+1):
			powers.append(a**b)

	return len(sorted(set(powers)))

print "Calculating number of distinct powers..."
print distinct_powers(100)