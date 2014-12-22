#!/usr/bin/env python
"""
Author: Denis Karanja,
Institution: The University of Nairobi, Kenya,
Department: School of Computing and Informatics, Chiromo campus
Email: dee.caranja@gmail.com,
Task: 4(Find the largest palindrome made from the product of two 3-digit numbers.)
License type: MIT :)
Status: COMPLETED...
"""
import time
startTime = time.clock()

def is_palindrome(num):
	reversed_num = str(num)[::-1]#reverse string
	if int(reversed_num) == num:
		return True
	else:
		return False

def multiple_palindrome(num_one = 100, num_two = 1000):
	(palindromes, limit) = ([], 1000)
	for i in range(limit + 1):
		if num_two >= 100:
			for j in range(limit +1):
				product = num_one * num_two
				if num_one < limit:
					if is_palindrome(product):
						palindromes.append(product)
				num_one += 1

		num_two -= 1
		num_one = 100
	return max(palindromes)

print "Calculating largest 3 digit product palindrome..."
print multiple_palindrome()
print "Run time... {} secs\n".format(round((time.clock() - startTime), 4))