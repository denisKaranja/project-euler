#!/usr/bin/python
"""
Author: Denis Karanja,
Institution: The University of Nairobi, Kenya,
Department: School of Computing and Informatics, Chiromo campus
Email: dee.caranja@gmail.com,
Task: 8(Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. 
	What is the value of this product?)
License type: MIT :)
Status: COMPLETED...
"""
import time
startTime = time.clock()

(product, lim, file_handle, sum_, g_product) = (1, 13, open("8_nums.txt", 'r'), 0, [])

def get_product(string):
	product = 1
	for i in string:
		product *= int(i)
	return product 

def one_string():
	string = ''
	for line in file_handle:
		line = line.strip()
		string += line
	return string

def read_13_digit(start, stop):
	string = one_string()

	for i in string:
		first = string[start:stop]

		if len(first) == 13:
			result = get_product(first)
			g_product.append(result)
			(start, stop) = (start + 1, stop + 1)
			read_13_digit(start, stop)

	return max(g_product)

print "Calculating..."
print(read_13_digit(0, 13))
print "Run time... {} secs\n".format(round((time.clock() - startTime), 4))