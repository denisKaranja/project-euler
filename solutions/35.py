#!/usr/bin/python
"""
Author: Denis Karanja,
Institution: The University of Nairobi, Kenya,
Department: School of Computing and Informatics, Chiromo campus
Email: dee.caranja@gmail.com,
Task: 35(Circular primes)
License type: MIT :)
Status: COMPLETED...
"""
def rotate(num):
	"""Rotates a number from left t rigth"""
	flag, num, length = (1, str(num), len(str(num)))

	for x in xrange(0, length):
		if x < length:
			new_num = int(num[x+1:] + num[0:x+1])
			if is_prime(new_num):
				flag *= 2
			else:
				flag = 0

	return(False, True)[flag >= 2]

def is_prime(num):
	"""Checks if a number is prime"""
	if num is 1:
		return False
	if num % 2 is 0:
		return num is 2

	division = 3
	while (division * division) <= num:
		if num % division is 0:
			return False
		division += 2
	return True

def main(limit):
	circular_sum = 13
	print("Calculating circular primes below {}".format(limit))
	for x in xrange(100, limit):
		if is_prime(x):
			if rotate(x):
				circular_sum += 1

	return circular_sum

if __name__ == "__main__":
	import time
	start = time.clock()
	print(main(1000000))
	print("Run time...{}(secs)".format(round(time.clock()-start, 5)))
