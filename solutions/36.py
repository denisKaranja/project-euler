#!/usr/bin/python
"""
Author: Denis Karanja,
Institution: The University of Nairobi, Kenya,
Department: School of Computing and Informatics, Chiromo campus
Email: dee.caranja@gmail.com,
Task: 36(Double base palindromes eg 585 and 1001001001 both in base 10 and 2 are palindromes))
License type: MIT :)
Status: COMPLETED...
"""
import time

def decimal_binary(num):
	"""Gets the binary equivalent of a number"""
	return "{:08b}".format(num)

def is_palindrome(num):
	"""Check if the number is a palindrome"""
	reversed_num = str(num)[::-1]
	if reversed_num == str(num): return True
	else: return False

def double_base_palindrome(limit = 1000000):
	"""Check if a decimal number and it's equivalent binary number are both palindromes"""
	(palindrome_sum, i) = (0, 1)
	for i in xrange(1, limit):
		if is_palindrome(i) and is_palindrome(int(decimal_binary(i))):
			palindrome_sum += i

	return palindrome_sum

print "Calculating sum of double base palindromes..."

startTime = time.clock()
print double_base_palindrome()

print "Run time... {}(secs)".format(round(time.clock() - startTime, 4))


