#!/usr/bin/python
"""
Author: Denis Karanja,
Institution: The University of Nairobi, Kenya,
Department: School of Computing and Informatics,
Email: dee.caranja@gmail.com,
Euler project solution = 347(Largest integer divisible by two primes)
Status.. PENDING...
"""
from time import time
def is_prime(num):
	"""Check if a number is prime"""
	if num == 1: return False
	for i in xrange(2, num):
		if num % i == 0 : return False
	else: return True


def get_primes(prime_limit, primes = []):
	"""Generate all primes in limit"""
	for j in xrange(1, prime_limit):
		if is_prime(j):
			primes.append(j)
	return primes

def max_val(my_list, maximum = 0):
	"""Returns a maximum value of a list"""
	for idx, val in enumerate(my_list):
		if my_list[idx] > maximum:
			maximum = my_list[idx]
	return maximum

def remove_primes(p_remv, q_remv, primes_list, new_primes = []):
	"""remove p and q in, primes_in_limit"""
	for k in primes_list:
		if (k != p_remv) and (k != q_remv):
			new_primes.append(k)
	return new_primes

def largest_int(p, q, limit = 100, results = []):
	"""Finds the largest int divisible by two primes where p and q are prime numbers"""
	primes_in_limit = get_primes(limit)
	new_primes = remove_primes(p, q, primes_in_limit)

	"""Get all ints divisible by p and q and other primes"""
	for l in xrange(1, limit):
		if l % p == 0 and l % q == 0:
			results.append(l)

	"""Get ints divisible by p and q only"""
	for val in new_primes:
		if results:
			if (max_val(results) % val) == 0:
				results.remove(max_val(results))
	return max_val(results)

def generate(gen_limit, sum_of_ints = 0, tuple_list = []):
	"""Generate a list of prime tuples p and q"""
	for p_gen in xrange(2, gen_limit):
		for q_gen in xrange(p_gen+1, gen_limit):
			if is_prime(p_gen) and is_prime(q_gen):
				tuple_list.append((p_gen, q_gen))

	"""Calculate the largest int"""
	for m in tuple_list:
		(x, y) = m
		#print (x,y), largest_int(x, y, 100)

	return tuple_list
#print generate(100)
print(largest_int(2, 61))
this_list = [(2, 3), (2, 5), (2, 7), (2, 11), (2, 13), (3, 5)]

# for i in this_list:
# 	(a, b) = i
# 	print (a, b), largest_int(a, b)
		