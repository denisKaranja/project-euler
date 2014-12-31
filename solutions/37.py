#!/usr/bin/python
"""
Author: Denis Karanja,
Institution: The University of Nairobi, Kenya,
Department: School of Computing and Informatics, Chiromo campus
Email: dee.caranja@gmail.com,
Task: 27(Truncatable primes eg 3797->379->37->3 and 3797->797->97->7)
License type: MIT :)
Status: PENDING...
"""
def is_prime(num):
	"""Check if a number is prime or not"""
	if num is 1:
		return False
	if num % 2 is 0:
		return num == 2
	division = 3
	while (division * division) <= num:
		if num % division == 0:
			return False
		division += 2

	return True

def truncate(num):
	"""Truncates a number digit by digit checking whether the new number is prime"""
	flag = 1
	if is_prime(num):
		length = len(str(num))
		for i in range(1, length):
			r_to_l = str(num)[0:i]
			l_to_r = str(num)[length-i:]
			r_to_l  =int(r_to_l)
			l_to_r = int(l_to_r)

			if is_prime(r_to_l) and is_prime(l_to_r):
				flag *= 2
			else:
				flag = 0

	return (0, num)[flag >= 2]

def main():
	truncs_sum, i, limit = [], 23, 1000000

	while i <= limit:
		if truncate(i) is not 0:
			truncs_sum.append(i)
		i += 1
		if len(truncs_sum) is 11:
			break
			
	return (len(truncs_sum), sum(truncs_sum))


if __name__ == "__main__":
	import time

	print "Calculating sum of the 11 truncatable primes..."
	start = time.clock()
	print main()
	print "Run time...{}(secs)".format(round(time.clock() - start, 5))