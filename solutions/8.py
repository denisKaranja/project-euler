#!/usr/bin/python
"""
Author: Denis Karanja,
Institution: The University of Nairobi, Kenya,
Department: School of Computing and Informatics, Chiromo campus
Email: dee.caranja@gmail.com,
Task: 8(Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. 
	What is the value of this product?)
License type: MIT :)
Status: PENDING...
"""

file_handle = open("8_nums.txt", 'r')
product = 0
string = '123456'
for line in file_handle:
	first = line[0:13]
	last = line[13:]
	print len(line)