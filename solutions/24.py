#!/usr/bin/python
"""
Author: Denis Karanja,
Institution: The University of Nairobi, Kenya,
Department: School of Computing and Informatics, Chiromo campus
Email: dee.caranja@gmail.com,
Task: 24(Lexicographic permutations)
License type: MIT :)
Status: COMPLETED...
"""
from itertools import permutations
import time
def generate(my_list):
	solutions = []
	for x in permutations(my_list):
		solutions.append(x)

	return str(sorted(solutions)[999999]).replace(", ", "")

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
start = time.clock()
print generate(a)
print "Run time...{}(secs)".format(round(time.clock()- start, 5))