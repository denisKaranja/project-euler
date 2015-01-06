#!/usr/bin/python
"""
Author: Denis Karanja,
Institution: The University of Nairobi, Kenya,
Department: School of Computing and Informatics,
Email: dee.caranja@gmail.com,
Euler project solution 41(Pandigital prime)
Status.. PENDING...
"""

def is_prime(num):
	"""Check if a number is prime"""
	if num is 1: return False
	if num % 2 is 0: return num is 2
	division = 3
	while (division * division) <= num:
		if num % division is 0:
			return False
		division += 2
	return True

def is_pandigit(num):
	"""Checks if a number is pandigital"""
	num, pandigit = str(num), ''
	length = len(num)
	'''generate a pandigit of length equal to num'''
	for x in xrange(1, length+1):
		pandigit += str(x)
	sorted_num = "".join(sorted(num))
	if sorted_num == pandigit: 
		return True
	else:
		return False

print(is_pandigit(7245361))