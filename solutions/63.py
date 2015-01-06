#!/usr/bin/python
"""
Author: Denis Karanja,
Institution: The University of Nairobi, Kenya,
Department: School of Computing and Informatics, Chiromo campus
Email: dee.caranja@gmail.com,
Task: 63(Powerful digit counts)
License type: MIT :)
Status: COMPLETED...
"""
def is_equal(num, power):
	"""Checks if the length of a number is equal to the power it is raised to"""
	if len(str(pow(num, power))) is power:
		return True
	else:
		return False

def main():
	n_dig_sum = 1#1^1=1
	for x in xrange(2, 10):
		for y in xrange(1, 22):
			if is_equal(x, y):
				n_dig_sum += 1

	return n_dig_sum

if __name__ == "__main__":
	print(main())

