#!/usr/bin/python
"""
Author: Denis Karanja,
Institution: The University of Nairobi, Kenya,
Department: School of Computing and Informatics, Chiromo campus
Email: dee.caranja@gmail.com,
Task: 12(What is the value of the first triangle number to have over five hundred divisors?)
License type: MIT :)
Status: PENDING...
"""

def recursive_tri(nth_term):
	if nth_term == 1 or nth_term == 0:
		return nth_term
	else:
		return  nth_term + recursive_tri(nth_term - 1)

def iterative_tri(num):
	num_sum = 0
	for i in range(1, num+1):
		num_sum += i
	return num_sum


for i in range( 11):
	print "{} ->> {}".format(i, iterative_tri(i))

