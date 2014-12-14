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
	new_num = str(num)[::-1]
	if int(new_num) == num:
		return True
	else:
		return False

is_palindrome(90099)