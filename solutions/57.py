#!/usr/bin/python
"""
Author: Denis Karanja,
Institution: The University of Nairobi, Kenya,
Department: School of Computing and Informatics, Chiromo campus
Email: dee.caranja@gmail.com,
Task: 57(Square roots convergents)
License type: MIT :)
Status: PENDING...
"""
def convergent(num, nth_expansion):
	"""Returns the nth expansion of a square root convergent"""
	sum_conve = 0
	for i in range(1, nth_expansion+1):
		sum_conve += 1 + (1./(2))

	print sum_conve

print convergent(2, 1)
