#!/usr/bin/python
"""
Author: Denis Karanja,
Institution: The University of Nairobi, Kenya,
Department: School of Computing and Informatics, Chiromo campus
Email: dee.caranja@gmail.com,
Task: 53(Combinatoric selections)
License type: MIT :)
Status: COMPLETED...
"""
import math

def combinatoric(n, r):
	"""Return the number of ways of selecting r from n"""
	return (math.factorial(n) / (math.factorial(r)*math.factorial(n - r)))

def main():
	combi_sum = 0
	for n in xrange(23, 101):
		for r in xrange(1, n):
			if n >= r:
				if combinatoric(n, r) > 1000000:
					combi_sum += 1

	return combi_sum

if __name__ == "__main__":
	import time
	start = time.clock()
	print(main())
	print("Run time...{}(secs)".format(round(time.clock()-start, 5)))
