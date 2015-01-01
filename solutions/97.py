#!/usr/bin/python
"""
Author: Denis Karanja,
Institution: The University of Nairobi, Kenya,
Department: School of Computing and Informatics, Chiromo campus
Email: dee.caranja@gmail.com,
Task: 97(Large non-Mersenne prime)
License type: MIT :)
Status: COMPLETED...
"""

def last_n(base, exp, n_last_digits):
	"""Returns The last n digits of a number raised to a bigger power"""
	fixed = 28433
	number = (fixed * pow(base, exp, pow(10, n_last_digits)) + 1) % pow(10, n_last_digits)
	
	return number
	
if __name__ == "__main__":
	import time
	print("Non-Mersene prime manipulation...(Last ten digits)")
	start = time.clock()
	print(last_n(2, 7830457, 10))
	done = time.clock()-start
	print("Run time...{}(secs)".format(round(done, 8)))
