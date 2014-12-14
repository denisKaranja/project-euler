#!/usr/bin/python
"""
Author: Denis Karanja,
Institution: The University of Nairobi, Kenya,
Department: School of Computing and Informatics, Chiromo campus
Email: dee.caranja@gmail.com,
Task: 4(Find the largest palindrome made from the product of two 3-digit numbers.)
License type: MIT :)
Status: PENDING...
"""
def is_palindrome(num):
	new_num = str(num)[::-1]#reverse string
	if int(new_num) == num:
		return True
	else:
		return False

palindromes = []

def multiplier_3_dig(num_one, num_two):
	limit = 999
	for i in xrange(1, limit+1):
		product = num_one * num_two
		if is_palindrome(product):
			palindromes.append(product)
			num_one += 1
			num_two += 1
		else:
			num_one += 1
			num_two += 1
	return palindromes




print multiplier_3_dig(100, 100)