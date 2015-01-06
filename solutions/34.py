#!/usr/bin/python
"""
Author: Denis Karanja,
Institution: The University of Nairobi, Kenya,
Department: School of Computing and Informatics, Chiromo campus
Email: dee.caranja@gmail.com,
Task: 34(Digit factorial)
License type: MIT :)
Status: COMPLETED...
"""
def factorial(num):
	"""Returns a factorial of a number"""
	fact = 1
	for x in xrange(1, num+1):
		fact *= x
	return fact

def fact_sum(num):
	"""Return the digit sum factorials of a number"""
	return sum([int(factorial(int(x))) for x in str(num)])

def main():
	digit_fact_sum, array = 0, []
	for x in xrange(3, 100000):
		if fact_sum(x) == x:
			array.append(x)
	return (array, sum(array))

print(main())
