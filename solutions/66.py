#!/usr/bin/python
"""
Author: Denis Karanja,
Institution: The University of Nairobi, Kenya,
Department: School of Computing and Informatics, Chiromo campus
Email: dee.caranja@gmail.com,
Task: 66(X^2 -Dy^2 = 1. find largest value of x for D  <= 1000 that satisfy the quadratic Diophantine equation)
License type: MIT :)
Status: PENDING...
"""
import time
def diophantine(D_limit):
	"""Return the largest value of X and the Value of D that gives that value"""
	(d, x_list, d_list, x_y_pairs) = (1, [], [], [])

	for x in xrange(1, D_limit*2):
		for y in xrange(1, D_limit*2):
			x_y_pairs.append((x, y))

	start = time.clock()
	"""Find values the satisfyn the equation"""
	for j in xrange(1, D_limit + 1):
		for pairs in x_y_pairs:
			x, y = pairs
			if ((x**2) - (d*(y**2))) is 1:
				x_list.append((x, y, d))
				#print max(x_list), "->>{}".format(time.clock() - start)
		d += 1



	return (sorted(x_list)[-4:])


print diophantine(1000)