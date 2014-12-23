#!/usr/bin/python
"""
Author: Denis Karanja,
Institution: The University of Nairobi, Kenya,
Department: School of Computing and Informatics, Chiromo campus
Email: dee.caranja@gmail.com,
Task: 9(Pythagorean triplet such that a^2 + b^2 = c^2 and a < b < c and a + b + c = 1000)
License type: MIT :)
Status: COMPLETED...
"""
import time
startTime = time.clock()

def is_pythagorean(a, b, c):
	return (a**2 + b**2 == c**2) and (a < b < c)

(a, b, c, array) = (0, 1, 2, [])


def find_pyth(a, b, c):
	for x in xrange(1000):
		for y in xrange(x + 1, 1000):
			for z in xrange(y +1, 1000):
				if is_pythagorean(x, y, z) and ((x + y + z) == 1000):
					return "{} from ->> {}".format(x*y*z, (x, y, z))
	

print "Calculating pythagorean triplet...\n"
print find_pyth(a, b, c)
print "Run time... {} secs\n".format(round((time.clock() - startTime), 4))


