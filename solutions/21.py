#!/usr/bin/python
"""
Author: Denis Karanja,
Institution: The University of Nairobi, Kenya,
Department: School of Computing and Informatics,
Email: dee.caranja@gmail.com,
Euler project solution 21(Amicable numbers)
Status.. COMPLETED...
"""
import time, math
def divisor_sum(num):
	"""Returns the sum of proper divisors of num that are less than the num"""
	factors, i = 0, (num-1)
	while i > 0:
		if num % i is 0:
			factors += i
			i -= 1
		else:
			i -= 1
	return(factors)

#revised sum(factors) fn()
def get_divisors(num):
	div_sum = 1
	for x in xrange(2, int(math.sqrt(num)) +1):
		if num % x == 0:
			div_sum += x
			div_sum += num/x
	return div_sum

def main(limit):
	print("Calculating amicable numbers sum below {}...".format(limit))
	amicable_sum = 0
	for i in xrange(1, limit):
		if i == get_divisors(get_divisors(i)) and (i != get_divisors(i)):
			amicable_sum += (i + get_divisors(i))

	return ((amicable_sum)/2)

if __name__ == "__main__":
	start = time.clock()
	print(main(10000))
	print("Run time...{}(secs)".format(round(time.clock()-start, 5)))

