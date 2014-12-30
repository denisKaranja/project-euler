#!/usr/bin/python
"""
Author: Denis Karanja,
Institution: The University of Nairobi, Kenya,
Department: School of Computing and Informatics, Chiromo campus
Email: dee.caranja@gmail.com,
Task: 304(Primonacci->> Next prime)
License type: MIT :)
Status: PENDING...
"""

def is_prime(num):
	"""Checks if a number is prime"""
	if num is 1:
		return False
	else:
		for i in xrange(2, num):
			if num % i is 0:
				return False
		else:
			return True

def next_prime(pos_int):
  """Returns the smallest prime (p) such that p > pos_int"""
  while True:
    pos_int += 1
    if is_prime(pos_int):
      return pos_int

def f_n(num):
	"""Return the fibonacci number"""
	x = i = 0
	y = z = 1
	for i in xrange(0, num+1):
		x = y
		y = z
		z = x + y
	return x

def a_n(n):
	"""Returns a(n) sequence"""
	if n is 1:
		return next_prime(10**14)
	else:
		return next_prime(a_n(n - 1))

def b_n(n):
	"""returns b(n) sequence"""
	return f_n(a_n(n))
	
def main():
	(limit, bn_sum, mod) = (100000, 0, 1234567891011)
	print "Calculating primonacci sum..."
	for i in xrange(1, limit+1):
		bn_sum += b_n(i)
		print bn_sum

	return (bn_sum % mod)

if __name__ == "__main__":
	import time
	start = time.clock()

	print next_prime(10**14)
	print "Run time...{}(secs)".format(round(time.clock()-start, 5))