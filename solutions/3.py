#!/usr/bin/python
"""
Author: Denis Karanja,
Institution: The University of Nairobi, Kenya,
Department: School of Computing and Informatics,
Email: dee.caranja@gmail.com,
Euler project solution = 3(Largest Prime factor of 600851475143)
Status.. COMPLETED
"""
import time
startTime = time.clock()

def is_prime(num):
	"""Check if a number is prime"""
	if num == 1:
		return False
	
	for x in xrange(2, num):
		if num % x == 0:
			return False

	else:
		return True


def largest_prime(number = 600851475143, output = []):
	"""Return the largest prime factor of number"""
	for i in xrange(1, number):
		if is_prime(i):
			if number % i == 0:
				output.append(i)
				print ("Prime num found->> {}".format(i))

	return max(output)

# print ("Calculating largest prime factor...")
# print ("\nLargest prime factor for 600851475143 is {}".format(largest_prime()))
# print ("Run time... {}\n".format(time.clock() - startTime))
def revised(number):
	"""A revised version"""
	(prime_factors, i) = ([], 2)
	while i <= number:
		i += 1
		if number % i is 0:
			prime_factors.append(i)
			number /= i

	return max(prime_factors)



print revised(600851475143)


