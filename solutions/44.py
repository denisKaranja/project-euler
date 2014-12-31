#!/usr/bin/python
"""
Author: Denis Karanja,
Institution: The University of Nairobi, Kenya,
Department: School of Computing and Informatics, Chiromo campus
Email: dee.caranja@gmail.com,
Task: 44(Pentagon numbers)
License type: MIT :)
Status: PENDING...
"""
def is_pentagon(num):
	"""Checks if a number is a pentagon number or not.
	Uses the formula Pn = n(3n-1)/2 or 3n^2 - n = 2Pn"""
	(a, b, c) = (3, -1, (2*-1*num))
	inner = (b)**2 - (4 * a * c)
	if 0 > inner:
		return False
	upper = (-b + pow(inner, 0.5))
	n = upper / (2.*(a))

	return (False, True)[float(n).is_integer()]

def pentagonal_pair(limit):
	"""Returns the pair of pentagonal numbers for which their sum and difference are pentagonal"""
	pentagon_nums, d_values = [], []
	for x in xrange(1, limit+1):
		for y in xrange(1, limit+1):
			if is_pentagon(x) and is_pentagon(y):
				z = x + y
				other_z = (y - x)
				if (is_pentagon(z)) and (is_pentagon(other_z)):
					d = abs(y - x)
					pentagon_nums.append((d, x, y))
					d_values.append(d)

	return (pentagon_nums)

def main():
	print pentagonal_pair(1000)

if __name__ == "__main__":
	import time
	print("Calculating pentagonal numbers...")
	start = time.clock()
	main()
	print("Run time..{}(secs)".format(round(time.clock()-start, 5)))