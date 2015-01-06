#!/usr/bin/python
"""
Author: Denis Karanja,
Institution: The University of Nairobi, Kenya,
Department: School of Computing and Informatics, Chiromo campus
Email: dee.caranja@gmail.com,
Task: 26(Reciprocal cycles)
License type: MIT :)
Status: COMPLETED...
"""

def find_recurring(denom, nume = 1):
	"""Returns the length of recuring digits"""
	assert denom > 0
	(int_div, rem, digits) = (nume // denom, nume % denom, [])
	seen = {rem: 0}
	while 1:
		rem *= 10
		digits.append(rem//denom)
		rem %= denom
		if rem in seen:
			recur_start = seen[rem]
			return (len(digits[recur_start:]))
		else:
			seen[rem] = len(digits)



def main():
	large_chain = []
	for denom in xrange(2, 1000):
		result = 1./denom
		large_chain.append((find_recurring(denom), denom))

	chain_len, d = max(large_chain)

	return d

if __name__ == "__main__":
	import time
	print("Calclulating the value 1/d that gives the longest recurring cycle")
	start = time.clock()
	print(main())
	print("Run time...{}(secs)".format(round(time.clock()-start, 5)))