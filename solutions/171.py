#!/usr/bin/python
"""
Author: Denis Karanja,
Institution: The University of Nairobi, Kenya,
Department: School of Computing and Informatics, Chiromo campus
Email: dee.caranja@gmail.com,
Task: 171(Finding numbers for which the sum of the squares of the digits is a square))
License type: MIT :)
Status: PENDING...
"""

num = 15
digit = 0
digit_sum = 0
i = 1

while i < num:
	for x in str(i):
		if len(str(i)) >= 2:
			for big_x in str(i):
				new_b_x = int(big_x) * int(big_x)
				print "Bix_X ->> %d -> %d" %(i, new_b_x)
		new_x = int(x) * int(x)
		print new_x

	i += 1

#print '\t',digit